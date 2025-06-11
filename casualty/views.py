
from rest_framework.response import Response
from .models import ERPatient
from .serializers import PatientSerializer
from datetime import datetime
from rest_framework.decorators import api_view , permission_classes
from pyauth.auth import HasRolePermission
from django.contrib.auth.hashers import make_password
from .models import Employee
from .serializers import EmployeeSerializer
from pymongo import MongoClient
from django.http import JsonResponse
import os
from dotenv import load_dotenv
from bson.json_util import dumps
from rest_framework.response import Response
from django.utils.dateparse import parse_date
from .models import ERPatient
from .serializers import PatientSerializer
from .models import ERPatientRegister
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .serializers import PatientRegisterSerializer
from datetime import date



load_dotenv()
#ER form 
@api_view(['POST'])
@permission_classes([HasRolePermission])
def create_patient(request):
    # Generate current and previous year in 2-digit format
    current_year = datetime.now().year % 100      # e.g. 2025 -> 25
    next_year = (datetime.now().year + 1) % 100    # e.g. 2026 -> 26
    prefix = f"{current_year:02d}{next_year:02d}"  # e.g. "2526"

    # Count how many patients already exist with this year's prefix
    existing_count = ERPatient.objects.filter(billNumber__startswith=prefix).count()
    next_number = existing_count + 1
    bill_number = f"{prefix}/{next_number:02d}"  # e.g. "2526/01", "2526/02"

    # Add the bill number into the request data
    data = request.data.copy()
    data['billNumber'] = bill_number

    serializer = PatientSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)



# views.py
@api_view(['GET'])
@permission_classes([HasRolePermission])
def get_procedure_list(request):
    mongo_url = os.getenv("GLOBAL_DB_HOST")
    client = MongoClient(mongo_url)
    db = client["Casuality"]
    collection = db["casualty_procedurelist"]

    procedures = list(collection.find({}))  # Fetch all records
    return JsonResponse(dumps(procedures), safe=False)




load_dotenv()
@api_view(['GET'])
@permission_classes([HasRolePermission])
def get_doctor_list(request):
    mongo_url = os.getenv("GLOBAL_DB_HOST")
    client = MongoClient(mongo_url)
    db = client["Casuality"]
    collection = db["casualty_casualty_doctors"]

    doctors = list(collection.find({"is_active": True}))  # Filter only active doctors
    return JsonResponse(dumps(doctors), safe=False)




@api_view(['GET'])
@permission_classes([HasRolePermission])
def get_next_bill_number(request):
    current_year = datetime.now().year % 100
    next_year = (datetime.now().year + 1) % 100
    prefix = f"{current_year:02d}{next_year:02d}"

    # Get latest billNumber with this prefix
    latest_patient = (
        ERPatient.objects.filter(billNumber__startswith=prefix)
        .order_by('-billNumber')
        .first()
    )

    if latest_patient:
        try:
            last_number = int(latest_patient.billNumber.split('/')[-1])
        except (IndexError, ValueError):
            last_number = 0
    else:
        last_number = 0

    next_number = last_number + 1
    next_bill_number = f"{prefix}/{next_number:02d}"
    return Response({'billNumber': next_bill_number})






@api_view(['GET'])
@permission_classes([HasRolePermission])
def get_patients_by_date(request):
    bill_date_str = request.GET.get('billDate')
    if not bill_date_str:
        return Response({"error": "billDate parameter is required"}, status=400)

    try:
        bill_date = parse_date(bill_date_str)
        if not bill_date:
            return Response({"error": "Invalid billDate format"}, status=400)

        patients = ERPatient.objects.filter(billDate=bill_date)
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

    





def get_next_er_number():
    today = date.today()
    year = today.year

    # Determine financial year start
    if today.month <= 3:
        start_year = year - 1
    else:
        start_year = year

    # Use last 2 digits of the year
    prefix = f"ER0{str(start_year)[-2:]}"

    # Filter by current financial year's prefix
    existing_ers = ERPatientRegister.objects.filter(erNumber__startswith=prefix).order_by('-erNumber')

    if existing_ers.exists():
        last_number = int(existing_ers[0].erNumber.split("/")[-1])
        next_number = last_number + 1
    else:
        next_number = 1

    return f"{prefix}/{str(next_number).zfill(6)}"


    # views.py


@csrf_exempt
@api_view(['POST'])
@permission_classes([HasRolePermission])
def register_patient(request):
    data = request.data.copy()
   
    serializer = PatientRegisterSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Patient Registered Successfully", "erNumber": data['erNumber']}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
def next_er_number(request):
    next_er = get_next_er_number()
    return Response({"erNumber": next_er})







@api_view(['POST'])
@permission_classes([HasRolePermission])
def register_employee(request):
    data = request.data.copy()
    data['password'] = make_password(data.get('password'))  # hash password
    serializer = EmployeeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Employee registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# views.py

@api_view(['POST'])
@permission_classes([HasRolePermission])
def login_employee(request):
    empid = request.data.get('empid')
    password = request.data.get('password')

    try:
        employee = Employee.objects.get(empid=empid)
        if check_password(password, employee.password):
            return Response({
                'message': 'Login successful',
                'empid': employee.empid,
                'name': employee.name,
                'role': employee.role,
                'email': employee.email
            }, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
    except Employee.DoesNotExist:
        return Response({'message': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)


# views.py

@api_view(['GET'])
@permission_classes([HasRolePermission])
def get_patient_by_er_number(request):
    er_number = request.query_params.get('erNumber')
    if not er_number:
        return Response({"error": "erNumber is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        patient = ERPatientRegister.objects.get(erNumber=er_number)
        serializer = PatientRegisterSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ERPatientRegister.DoesNotExist:
        return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)


#printbill


@api_view(['GET'])
@permission_classes([HasRolePermission])
def fetch_er_patient_bills(request):
    selected_date = request.GET.get('date')
    try:
        if selected_date:
            selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
        else:
            selected_date = datetime.today().date()

        patients = ERPatient.objects.filter(billDate=selected_date)
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=400)

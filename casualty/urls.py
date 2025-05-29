from django.urls import path
from . import views 

urlpatterns = [
    path('patient/', views.create_patient,name='create_patient'),
    path('patients/register/', views.register_patient, name='register_patient'),
      path('employeeregister/', views.register_employee, name='register_employee'),
      path('login/', views.login_employee),
     path('next-bill-number/', views.get_next_bill_number),
     path("next-er-number/", views.next_er_number),
     path('dashboard/', views.get_patients_by_date),
    path("procedures/", views.get_procedure_list, name="procedure-list"),
     path("doctors/", views.get_doctor_list, name="doctor-list"),
     path('patient-by-er/', views.get_patient_by_er_number, name='patient-by-er'),
     path('patients-by-date/', views.get_patients_by_date, name='patients-by-date'),
    path('printbill/', views.fetch_er_patient_bills, name='fetch_er_patient_bills'),

]

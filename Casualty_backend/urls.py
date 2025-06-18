# Casualty_backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('_b_a_c_k_e_n_d/Casualty/', include('casualty.urls')),
    path('', include('casualty.urls')),

]

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('doctor/', views.doctor_dashboard, name='doctor_dashboard'),
    path('patient/', views.patient_dashboard, name='patient_dashboard'),
    path('logout/', views.logout_view, name='logout'),
]
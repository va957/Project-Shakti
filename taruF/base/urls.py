from django.urls import path

from . import views

urlpatterns = [
    # path('login/', views.loginPage, name="login"),
    #path('logout/', views.logoutUser, name="logout"),
    # path('form/',views.form_view,name="form_view"),
    path('patient-detail/',views.patient_detail,name="patient_detail"),
    path ('doctor-dashboard/',views.doctor_dashBoard,name="doctor_dashBoard"),
    path ('home/',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('rmp/',views.rmp_dashbaord,name="rmp"),
    

path('', views.home, name='home'),
    path('diseaseprediction', views.disease, name='diseaseprediction'),
]

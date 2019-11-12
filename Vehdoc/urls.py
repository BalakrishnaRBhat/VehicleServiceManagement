from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('cust_reg/', views.customer_register, name='cust-reg'),
    path('ser_reg/', views.service_register, name='ser-reg'),
    path('login/', views.login, name='login'),
    path('cust_log/', views.customer_login, name='cust-log'),
    path('ser_log/', views.service_login, name='ser-log'),
    path('logout/',views.log_out,name='logout'),
    path('cust_dash/',views.cust_dash,name='cust-dash'),
    path('cust_profile/',views.cust_profile,name='cust-profile'),
    path('ser_dash/',views.ser_dash,name='ser-dash'),
    path('ser_profile/',views.ser_profile,name='ser-profile'),
    path('create_booking/',views.booking,name='create-booking'),
    path('bookings_view/',views.bookings_view,name='bookings-view'),
    path('service_view',views.service_view,name='service-view'),
    path('update_status/',views.udpate_status,name='update-status')

]
from django.shortcuts import render,reverse,redirect
from django.contrib import messages
from django.db import connection
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from .models import ServiceStation,Service,Customer,Vehicle
from .forms import (CustomerRegistrationForm,
CustomerInfoForm,ServiceStationRegistrationForm,ServiceStationInfoForm,ServiceStationLoginForm,CustomerLoginForm,VBooking)


def home(request):
    return render(request,'home.html')
def register(request):
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')

def customer_register(request):
    cus_form = CustomerRegistrationForm()
    cus_info_form = CustomerInfoForm()
    if request.method == 'POST':
        cus_form = CustomerRegistrationForm(request.POST)
        cus_info_form = CustomerInfoForm(request.POST)
        if cus_form.is_valid() and cus_info_form.is_valid():
            username = cus_form.cleaned_data['username']
            first_name = cus_info_form.cleaned_data['first_name']
            last_name = cus_info_form.cleaned_data['last_name']
            email = cus_info_form.cleaned_data['email']
            cust_phone = cus_info_form.cleaned_data['cust_phone']
            address = cus_info_form.cleaned_data['address']
            if cus_form.cleaned_data['password'] == cus_form.cleaned_data['password_confirm']:
                new_cust = User.objects.create(
                   username=username,
                   is_superuser=False
                )
                new_cust.set_password(cus_form.cleaned_data['password'])
                new_cust.save()
                new_cus_info = Customer()
                new_cus_info.cust_id = new_cust
                new_cus_info.first_name = first_name
                new_cus_info.last_name = last_name
                new_cus_info.email = email
                new_cus_info.address = address
                new_cus_info.cust_phone = cust_phone
                new_cus_info.save()
                
                
                return redirect('home')
        else:
            cus_form = CustomerRegistrationForm()
            cus_info_form = CustomerInfoForm()
    context = {
        'cus_form': cus_form,
        'cus_info_form': cus_info_form
    }
    return render(request,'customer_reg.html',context)

def service_register(request):
    ser_form = ServiceStationRegistrationForm()
    ser_info_form = ServiceStationInfoForm()
    if request.method == 'POST':
         ser_form = ServiceStationRegistrationForm(request.POST)
         ser_info_form = ServiceStationInfoForm(request.POST)
         if ser_form.is_valid() and ser_info_form.is_valid():
             username = ser_form.cleaned_data['username']
             station_name = ser_info_form.cleaned_data['station_name']
             email = ser_info_form.cleaned_data['email']
             ss_phone = ser_info_form.cleaned_data['ss_phone']
             address = ser_info_form.cleaned_data['address']
             if ser_form.cleaned_data['password'] == ser_form.cleaned_data['password_confirm']:
                 if User.objects.filter(username=username).exists():
                     messages.info(request,'Username Taken..')
                 elif User.objects.filter(email=email).exists():
                     messages.info(request,'Email Taken..')
                 else:
                    new_ser = User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=ser_form.cleaned_data['password'],
                    is_superuser=True
                    )
                 new_ser.save()
                 new_ser_info = ServiceStation()
                 new_ser_info.station_name = station_name
                 new_ser_info.stat_id = new_ser
                 new_ser_info.email = email
                 new_ser_info.address = address
                 new_ser_info.ss_phone = ss_phone
                 new_ser_info.save()
                 return redirect('home')                 
             else:
                 messages.info(request,'Password not matching')

             ser_form = ServiceStationRegistrationForm()
             ser_info_form = ServiceStationInfoForm()
    context = {
        'ser_form': ser_form,
        'ser_info_form': ser_info_form
    }
    return render(request,'service_reg.html',context)
def customer_login(request):
    cust_log = CustomerLoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            request.session['uname'] = username
            auth.login(request,user)  
            return redirect('cust-dash')
                
        else:
             msg = 'Username or Password Incorect'
             context = {
                'cust_log':cust_log,
                'msg':msg}
             return render(request,'customer_log.html',context)
                
    context = {
        'cust_log': cust_log
    }
    return render(request, 'customer_log.html', context)
def service_login(request):
    ser_log = ServiceStationLoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser == True:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('ser-dash')
                
        else:
             msg = 'Username or Password Incorect '
             context = {
                'ser_log':ser_log,
                'msg':msg}
             return render(request,'service_log.html',context)
                
    context = {
        'ser_log': ser_log,
    }
    return render(request, 'service_log.html', context)
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

#customer dashboard view
def cust_dash(request):
    return render(request,'cust_dash.html')    

def cust_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    context = {
        'user':user
    }
    return render(request,'cust_profile.html',context)

#service cemter dashboard view
def ser_dash(request):
    return render(request,'ser_dash.html')

def ser_profile(request,pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    context = {
        'user':user
    }
    return render(request,'ser_profile.html',context)

def booking(request):
    form = VBooking()
    if request.method == 'POST':
        form = VBooking(request.POST)
        if form.is_valid():
            cust = request.user.customer
            cust.save()
            vehicle_reg_no = form.cleaned_data['vehicle_reg_no']
            vehicle_name = form.cleaned_data['vehicle_name']
            vehicle_type = form.cleaned_data['vehicle_type']
            type_of_service = form.cleaned_data['type_of_service']
            service_desc = form.cleaned_data['service_desc']
            ser_status = 'Waiting'
            v = Vehicle.objects.create_vehicle(vehicle_reg_no=vehicle_reg_no,vehicle_name=vehicle_name,vehicle_type=vehicle_type,owner=cust)
            v.save()
            s = Service.objects.create_service(veh=v,type_of_service=type_of_service,service_desc=service_desc,ser_status=ser_status,ss=cust)
            s.save()
            return redirect('cust-dash')
    else:
        form = VBooking()
    context = {
        'form':form
    }
    return render(request,'create_booking.html',context)
#bookings view for customer 
def bookings_view(request):
        cust = request.user.customer
        booking_list = Vehicle.objects.bookings(cust)
        service_list = Service.objects.services(cust)
        context = {
            'booking_list': booking_list,
            'service_list': service_list
        }
        return render(request,'bookings_view.html',context)
# service view for service station
def service_view(request):
    ser = Service.objects.all()
    context = {
        'ser': ser
    }
    return render(request,'service_view.html',context)

# status udpattion procedure call for updating status of service 
def udpate_status(request):
    if request.method == 'POST':
        service_id = int(request.POST['service_id'])
        status = request.POST['status']
        cursor = connection.cursor()
        cursor.execute("call update_status(%s,%s)",(service_id,status))
        return redirect('service-view')
    return render(request,'update_status.html')
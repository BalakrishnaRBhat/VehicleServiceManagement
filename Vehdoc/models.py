from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save

#Ouery helper
class BookinQuerySet(models.QuerySet):
    def bookings(self, owner=None):
        if owner:
            return self.filter(owner=owner)
        return self
class ServiceQuerySet(models.QuerySet):
    def services(self, ss=None):
        if ss:
            return self.filter(ss=ss)
        return self

#Vehicle Manager
class VehicleManager(models.Manager):
    def create_vehicle(self,vehicle_reg_no,vehicle_name,vehicle_type,owner):
        return self.create(vehicle_reg_no=vehicle_reg_no,vehicle_name=vehicle_name,vehicle_type=vehicle_type,owner=owner)
    def get_queryset(self):
        return BookinQuerySet(self.model,using=self._db)
    def bookings(self,owner=None):
        if owner:
            return self.get_queryset().bookings(owner=owner)
        return self.get_queryset().bookings()

#Service Manager
class ServiceManager(models.Manager):
    def create_service(self,veh,type_of_service,service_desc,ser_status,ss):
        return self.create(veh=veh,type_of_service=type_of_service,service_desc=service_desc,ser_status=ser_status,ss=ss)
    def get_queryset(self):
        return ServiceQuerySet(self.model,using=self._db)
    def services(self,ss=None):
        if ss:
            return self.get_queryset().services(ss=ss)
        return self.get_queryset().services()

#Customer model
class Customer(models.Model):
    cust_id = models.OneToOneField(to=User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cust_phone = models.CharField(max_length=12)
    address = models.CharField(max_length = 100)
       
# ServiceStation model
class ServiceStation(models.Model):
    stat_id = models.OneToOneField(to=User,on_delete=models.CASCADE)  
    station_name = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    address = models.CharField(max_length=100)
    ss_phone = models.CharField(max_length=12)

#Vehicle model
class Vehicle(models.Model):
    vehicle_reg_no = models.CharField(max_length=10)
    vehicle_name = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=20)
    owner = models.ForeignKey(to=Customer,on_delete=models.CASCADE)
    objects = VehicleManager()

#Service model
class Service(models.Model):
    service_status = (('Waiting','Waiting'),('In progress','In progress'),('Completed','Completed'))
    ss = models.ForeignKey(to=Customer,on_delete=models.CASCADE)
    ser = models.ForeignKey(to=ServiceStation,on_delete=models.CASCADE,null=True)
    veh = models.OneToOneField(to=Vehicle,on_delete=models.CASCADE,null=True)
    type_of_service = models.CharField(max_length=50,null=True)
    service_desc = models.CharField(max_length=100,null=True)
    ser_status = models.CharField(max_length=100,choices=service_status,null=True)
    start_date = models.DateTimeField(null=True)
    finish_date = models.DateTimeField(null=True)
    objects = ServiceManager()




    
     
       
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from doctor.models import Doctor
from .models import Appointment
from .models import Patient
from django.contrib import messages


def patindex(request):
    return render(request,'patient.html')

def pregs(request):
    return render(request,'patindex.html')

def psignup(request):
    name=request.POST['name']
    email=request.POST['email']
    password=request.POST['password']
    mob=(int)(request.POST['mob'])
    gen=request.POST['gen']
    age=(int)(request.POST['age'])
    dis=request.POST['dis']
    user=Patient(name=name,email=email,password=password,mob=mob,gen=gen,age=age,dis=dis)
    user.save()
    u=User.objects.create_user(first_name=name,username=name,password=password,email=email)
    u.save()
    return redirect('patindex')

def plogin(request):
    username=request.POST['username']
    password=request.POST['password']
    user=auth.authenticate(username=username,password=password)
    messages.info(request,'Invalid Username or Password')
    #user=Patient(email=email,password=password)
    if user is not None:
        auth.login(request,user)
        doc=Doctor.objects.all()
        return render(request,'phome.html',{'doc':doc})
    else:
        return render(request,'patient.html')
        
def searchdoc(request):
    spcl=request.GET['spcl']
    doc=Doctor.objects.get(spcl=spcl)
    return render(request,'docserch.html',{'doc':doc})

def bookappoint(request):
    dname=request.POST['dname']
    pname=request.POST['pname']
    date=request.POST['date']
    time=request.POST['time']
    if Appointment.objects.filter(date=date).exists() and Appointment.objects.filter(time=time):
        return render(request,"docserch.html")
    else:
        ap=Appointment(dname=dname,pname=pname,date=date,time=time)
        ap.save()
        return render(request,'phome.html')
        
def showpres(request):
    pname=request.GET['uname']
    pat=Appointment.objects.all().filter(pname=pname)    
    return render(request,'showpres.html',{'pat':pat})   
# Create your views here.
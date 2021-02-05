from django.shortcuts import render, redirect
from django.views import View
from patient.models import Appointment
from .models import Doctor
from django.contrib import auth, messages


def docindex(request):
    return render(request, 'docindex.html')


class Login(View):
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        # doctor = Doctor.get_doc_obj(username)
        if Doctor.objects.filter(name=username).exists() and Doctor.objects.filter(password=password).exists():
            doc = Doctor.objects.get(name=username)
            return render(request, 'dhome.html', {'': doc})
        else:
            messages.info(request, 'Invailid Username or Password')
            return render(request, 'docindex.html')


def getdocappoint(request):
    date = request.POST['date']
    time = request.POST['time']
    pat = Appointment.objects.get(date=date, time=time)
    return render(request, 'todayappoint.html', {'pat': pat})


def priscribed(request):
    dname = request.POST['dname']
    pname = request.POST['pname']
    date = request.POST['date']
    time = request.POST['time']
    pres = request.POST['pres']
    Appointment.objects.filter(
        dname=dname, pname=pname, date=date, time=time).update(pres=pres)
    print("updated")
    return render(request, 'dhome.html')


def index(request):
    return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect("/")

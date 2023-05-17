from django.shortcuts import render
from .models import Departments,Doctors
from .forms import BookingForm
from  django.http import  HttpResponse
# Create your views here.
def index(request):
    #person={
    #   'name':'john',
    #    'age':36,
    #    'place':'ernakulam'
    #}

    #numbers={
    #    'num1':0
    #}

    #oddoreven={
    #    'num2':3
    #}

    numbers={
        #'num1':[1,2,3,4,5,6,7,8,9,10]
        'fruits':['mango','apple','banana','orange']

             }

    #return HttpResponse("Home Page")
    #return render(request, 'index.html',person)
    return render(request, 'index.html', numbers)
    #return render(request, 'index.html', oddoreven)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)

def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)

def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)
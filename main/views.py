from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):

    #When the user clicks on the website, the homepage shows up
    if request.method == 'GET':
        return render(request, 'NTCC/home.html')

    #If the user fills and submits the form
    elif request.method == 'POST':
        #Taking Inputs from user in Post method
        Age=int(request.POST['Age'])
        Weight=int(request.POST['Weight'])
        Height=int(request.POST['Height'])
        Gender=request.POST['gender']

        # Calculation According to gender
        if (Gender == 'male'):
            BMR=round((Weight*10)+(Height*6.25)-(Age*5)+(5))
        else:
            BMR=round((Weight*10)+(Height*6.25)-(Age*5)+(161))

        #Calculation According to Activity Level
        Activity=request.POST['Activity']

        if (Activity == '1'):
            Calories=(BMR*1.3)
        elif (Activity == '2'):
            Calories=(BMR*1.5)
        elif (Activity == '3'):
            Calories=(BMR*1.7)

        #Drop down for checking if its for Loosing weight or gaining muscle
        TypeOfCal=request.POST['CalType']

        #Cutting Calories
        if (TypeOfCal == 'cutting'):
            Calorie=round(Calories-250)
        elif (TypeOfCal == 'gaining'):
            #Surplus Calories
            Calorie=round(Calories+250)

    context = {'BMR': BMR, 'Cal':Calories, 'Calorie':Calorie}
    return render(request, 'NTCC/home.html',context)

def CountCal(request):
    
     return render(request, 'NTCC/CountCal.html', context)

from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def reqistration(request):
    return render(request, 'registration.html')

def makeNewPlan(request):
    return render(request,'makeNewPlan.html')

def plan(request):
    return render(request,'plan.html')

def listOfPlans(request):
    return render(request,'listOfPlans.html')




# for managers

def managerReport(request):
    return render(request,'manager/report.html')
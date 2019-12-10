from django.shortcuts import render,redirect
#from django.http import HttpResponse
from .models import emp
from .forms import EmployeeForm
# Create your views here.

def employ(request):
    
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form=EmployeeForm()
        return render(request,'index.html',{'form':form})
def show(request):
    em=emp.objects.all()
    return render(request,'show.html',{'em':em})
    
    
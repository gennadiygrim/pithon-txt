from django.shortcuts import render
#from django.http import HttpResponse
 
from .models import Task
from .forms import TaskForm
#tasks = Task.objects.all()
tasks = Task.objects.order_by('id')
#tasks = Task.objects.order_by('id')[:2]
def index(request):
    return render(request,'main/index.html',{'title':'Главная страница сайта','tasks':tasks})

def about(request):
    #return HttpResponse("<h4>About</h4>")
    return render(request,'main/about.html')

def create(request):
    #return HttpResponse("<h4>About</h4>")
    form=TaskForm()
    context = {'form':form}
    return render(request,'main/create.html',context)
    

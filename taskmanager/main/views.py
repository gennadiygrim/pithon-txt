from django.shortcuts import redirect, render
#from django.http import HttpResponse
 
from .models import Task
from .forms import TaskForm
#tasks = Task.objects.all()
tasks = Task.objects.order_by('id')
#tasks = Task.objects.order_by('id')[:2]
def index(request):
    tasks = Task.objects.order_by('id')
    return render(request,'main/index.html',{'title':'Главная страница сайта','tasks':tasks})
def about(request):
    #return HttpResponse("<h4>About</h4>")
    return render(request,'main/about.html')

def create(request):
    erorr=''
    if (request.method=='POST'):
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            erorr='Форма была не верной'
    #return HttpResponse("<h4>About</h4>")
    form=TaskForm()
    context = {'form':form,
               'erorr':erorr
               }
    
    
    return render(request,'main/create.html',context)
    

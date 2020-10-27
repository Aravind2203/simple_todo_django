from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Todolist
from .forms import create_form
# Create your views here.
def home(request):

	tasks=Todolist.objects.all()
	return render(request,'home.html',context={"tasks":tasks})

def add_task(request):
	task_to_be_done=request.POST['content']
	t=Todolist(task=task_to_be_done)
	t.save()
	return redirect('/')
def delete_task(request,id):
	task_object=Todolist.objects.get(id=id).delete()
	return redirect('/')
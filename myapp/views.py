from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import TaskModel

# Create your views here.

def home(request):

  data = TaskModel.objects.all().values()
  data_dict = {
    'data':data
  }
  return render(request,"home.html",data_dict)




def addTask(request):
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8')) 
        task = body.get("task")
        date = body.get('date')

        
        newDoc = TaskModel(task = task, date = date)
        
        newDoc.save()

        return HttpResponse(body)
        
        
        
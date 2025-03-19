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

  print(data_dict)
  
  return render(request,"home.html",data_dict)

def homeDate(request):

  if request.method  == "POST":
    body = json.loads(request.body.decode('utf-8'))
    date = body.get('date')
    tasks = TaskModel.objects.filter(date=date)
    data = []


    for i in tasks:
      print(i.date)
      obj = {
        "task":i.task,
        "date":i.date,
        "done":i.done,
        "sino":i.sino
      }
      data.append(obj)
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
        
def taskDone(request):
  if request.method == "POST":
    body = json.loads(request.body.decode('utf-8'))
    sino = body.get('sino')
    doneTask = TaskModel.objects.get(sino = sino )
    doneTask.done = True
    doneTask.save()
    print("doneTask:::::: ",doneTask.done)

def taskUndone(request):
  if request.method == "POST":
    body = json.loads(request.body.decode('utf-8'))
    sino = body.get('sino')
    doneTask = TaskModel.objects.get(sino = sino )
    doneTask.done = False
    doneTask.save()
    print("doneunTask:::::: ",doneTask.done)


def taskDelete(request):
  if request.method == "POST":
    body = json.loads(request.body.decode('utf-8'))
    sino = body.get('sino')
    task = TaskModel.objects.get(sino = sino)
    task.delete()

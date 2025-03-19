from django.urls import path
from . import views

urlpatterns=[
  path('',views.home),
  path('addTask/',views.addTask),
  path('taskDone/',views.taskDone),
  path('taskUndone/',views.taskUndone),
  path('taskDelete/',views.taskDelete),
  path('homeDate/',views.homeDate)
]
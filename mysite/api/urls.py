from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_viewer, name="api viewer"),
    path('task-list', views.task_list, name="Task List"),
    path('add-task', views.save_task, name="Add Task"),
    path('task-detail/<str:pk>', views.task_detail, name="Detail Task"),
    path('task-update/<str:pk>', views.task_update, name="Update Task"),
    path('task-delete/<str:pk>', views.task_delete, name="Delete Task"),
]

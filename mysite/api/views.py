# pylint: disable=no-member
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
def api_viewer(request):
    api_urls = {
        'TaskList': '/task-list',
        'AddTaskList': '/add-task',
        'DetailTskList': '/task-detail/<str:pk>',
        'UpdateTaskList': '/task-update/<str:pk>',
        'deleteTaskList': '/task-delete/<str:pk>',
    }
    return Response(api_urls)


@api_view(['POST'])
def save_task(request):
    serializer = TaskSerializer(data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def task_list(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("delete ok")

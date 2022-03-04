from django.urls import path

from .views import *

app_name = "tasks"

urlpatterns = [
    path('', TaskListView.as_view(), name='api-list-tasks')
]

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.models import Task
from tasks.api.serializers import TaskSerializer


class TaskListView(generics.ListAPIView):
    """
    view to list all tasks of current user
    """
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        if self.request.GET.get('status', None):
            if self.request.GET.get('status') == 'pending':
                return Task.objects.filter(end_user=self.request.user, status=Task.PENDING)
            elif self.request.GET.get('status') == 'finished':
                return Task.objects.filter(end_user=self.request.user, status=Task.FINISHED)
            elif self.request.GET.get('status') == 'overdue':
                return Task.objects.filter(end_user=self.request.user, status=Task.OVERDUE)
            elif self.request.GET.get('status') == 'unfinished':
                return Task.objects.filter(end_user=self.request.user, status__in=[Task.PENDING, Task.OVERDUE])

        return Task.objects.filter(end_user=self.request.user)

    def get(self, request, *args, **kwargs):
        response = super(TaskListView, self).get(request, *args, **kwargs)

        return Response({
            "status": status.HTTP_200_OK,
            'message': 'success',
            'data': response.data
        })


class CompleteTaskView(APIView):
    """
    view for mark task as finished
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            task.mark_finished()
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={
                "status": status.HTTP_404_NOT_FOUND,
                'message': 'task not found',
                'data': []
            })
        return Response({
            "status": status.HTTP_200_OK,
            'message': 'task marked as completed successfully',
            'data': []
        })


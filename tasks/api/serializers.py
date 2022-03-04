from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    serializer for tasks list
    """
    class Meta:
        model = Task
        read_only_fields = ['id', 'created_at']
        fields = [
            'id',
            'title',
            'description',
            'end_user',
            'status',
            'due_date',
            'created_at',
            'updated_at'
        ]

from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """
    This model to save tasks of end users
    """

    # STATUS CHOICES
    PENDING = 'P'
    FINISHED = 'F'
    OVERDUE = 'D'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (FINISHED, 'Finished'),
        (OVERDUE, 'OverDue'),
    ]

    title = models.CharField(
        'Title',
        max_length=70,
    )
    description = models.CharField(
        'Description',
        max_length=500,
        blank=True,
        null=True
    )
    status = models.CharField(
        'Status',
        max_length=1,
        choices=STATUS_CHOICES,
        default=PENDING
    )
    due_date = models.DateTimeField(
        'Due Date',
        null=True,
        blank=True
    )
    end_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='my_tasks',
        verbose_name='End User'
    )
    created_at = models.DateTimeField(
        'Created At',
        auto_now_add=True,
        null=True,
        blank=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        'Updated At',
        auto_now=True,
        null=True,
        blank=True,
        db_index=True
    )

    class Meta:
        get_latest_by = '-created_at'
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return str(self.title)

    def mark_finished(self):
        """Mark task as finished or completed"""
        self.status = self.FINISHED
        self.save()

# -*- coding: utf-8 -*-
"""api models."""
from django.db import models
from django.utils import timezone
from .constants import TASK_STATE_CHOICES, NOT_DONE_STATE
# Create your models here.


class Task(models.Model):
    """Task model."""

    state = models.IntegerField(
        default=NOT_DONE_STATE,
        choices=TASK_STATE_CHOICES
    )
    text = models.TextField()
    due_date = models.DateTimeField(
        blank=True,
        null=True
    )
    created_on = models.DateTimeField(
        auto_now=True
    )
    updated_on = models.DateTimeField(
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        """Update times."""
        self.modified = timezone.now()
        return super(Task, self).save(*args, **kwargs)

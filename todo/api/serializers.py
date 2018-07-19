# -*- coding: utf-8 -*-
"""serializers for api."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer class for Task model."""

    class Meta:
        """Meta for TaskSerializer."""

        model = Task
        fields = ('state', 'text', 'due_date')
        read_only_fields = ('id',)

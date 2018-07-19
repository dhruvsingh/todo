# -*- coding: utf-8 -*-
"""serializers for api."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer class for Task model."""

    state_display = serializers.SerializerMethodField()

    class Meta:
        """Meta for TaskSerializer."""

        model = Task
        fields = ('id', 'state', 'text', 'due_date', 'state_display')
        read_only_fields = ('id', 'state_display')

    def get_state_display(self, obj):
        """State Display to show meaningful state."""
        return obj.get_state_display()

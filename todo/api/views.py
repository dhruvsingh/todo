# -*- coding: utf-8 -*-
"""views for api."""
from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer

from django_filters.rest_framework import DjangoFilterBackend


class TaskViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Task to be viewed, listed, added or edited."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backend = (DjangoFilterBackend,)
    filter_fields = ('state', 'due_date')

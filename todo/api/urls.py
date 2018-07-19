# -*- coding: utf-8 -*-
"""urls for api."""
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(r'task', views.TaskViewSet)

urlpatterns = router.urls

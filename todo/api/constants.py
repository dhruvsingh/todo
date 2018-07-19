# -*- coding: utf-8 -*-
"""contants for api."""
from django.utils.translation import gettext_lazy as _

NOT_DONE_STATE = 1
DONE_STATE = 2

DONE_TEXT = "Done"
NOT_DONE_TEXT = "Not Done"

TASK_STATE_CHOICES = (
    (NOT_DONE_STATE, _(NOT_DONE_TEXT)),
    (DONE_STATE, _(DONE_TEXT)),
)

# -*- coding: utf-8 -*-
from django.urls import path

from .views import add_comment_view, mark_to_delete, mark_to_read, notification_view

urlpatterns = [
    path("add/", add_comment_view, name="add_comment"),
    path("notification/", notification_view, name="notification"),
    path(
        "notification/no-read/",
        notification_view,
        {"is_read": "false"},
        name="notification_no_read",
    ),
    path("notification/mark-to-read/", mark_to_read, name="mark_to_read"),
    path("notification/mark-to-delete/", mark_to_delete, name="mark_to_delete"),
]

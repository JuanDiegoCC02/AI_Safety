from django.urls import path
from .views import (ModerationResultListCreateView)

# Create your urls here.

urlpatterns = [

    path(
        'moderation/',
        ModerationResultListCreateView.as_view(),
        name='moderation'
    ),
]
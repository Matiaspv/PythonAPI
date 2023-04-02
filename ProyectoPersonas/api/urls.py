from django.urls import path
from .views import PersonaView

urlpatterns=[
    path('personas/',PersonaView.as_view(), name='personas_list')
]
# We sill store the urls local to this app
from django.urls import path
from .views import RoomView

urlpatterns = [
    path('room', RoomView.as_view()), # .as_view() means send the class as a view
]

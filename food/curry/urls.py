from django.urls import path
from curry.views import home
urlpatterns = [
    path('',home),
]

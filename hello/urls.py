from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("chukwudi", views.chukwudi, name="chukwudi"),
    path("moyra", views.moyra, name="moyra"),
    path("<str:name>", views.greet, name="greet")
]
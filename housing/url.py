from django.urls import path
from housing import views as v
urlpatterns = [
    path("", v.index),
    path("evolution", v.evolution)
]

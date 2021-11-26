from django.contrib import admin
from django.urls import path

# edited by me 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # edited by me 
    path("", views.index),
    path("test", views.testCricket)
]

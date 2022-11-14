from django.urls import path

from . import views

urlpatterns = [
    path('<invite_token>', views.index, name='index'),
]
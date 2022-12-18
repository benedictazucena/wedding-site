from django.urls import path

from . import views

urlpatterns = [
    path('rsvp', views.rsvp, name='rsvp'),
    path('logout', views.logout, name='logout'),
    path('gift', views.gift, name='gift'),
    path('live', views.live, name='live'),
    path('<invite_token>', views.index, name='index'),
    path('', views.index, name='index'),


]
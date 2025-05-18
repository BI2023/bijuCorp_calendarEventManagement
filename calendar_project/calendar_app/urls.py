# calendar_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='calendar_view'),
    path('add/', views.event_create, name='event_add'),
    path('events/<int:year>/<int:month>/<int:day>/', views.events_by_date, name='events_by_date'),
]

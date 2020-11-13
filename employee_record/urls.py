
from django.urls import path
from . import views
urlpatterns = [
    path('',  views.update_employees, name='update_employees'),
    path('list/', views.view_employees, name='view_employees')
]
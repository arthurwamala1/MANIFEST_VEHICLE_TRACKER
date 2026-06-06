from django.urls import path
from . import views

urlpatterns = [

path('',views.dashboard,name='dashboard'),

path(
'add-bus/',
views.add_bus
),

path(
'subtract-bus/',
views.subtract_bus
),

]
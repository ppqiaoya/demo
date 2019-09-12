from django.urls import path
from app01 import views
from .views import *

urlpatterns = [
    path('ss/', views.ss),
    path('add/',views.add),
    path('query/',views.query),
    path('update/',views.update),
    path('delete/',views.delete),
    path('scx/',views.scx),
    path('yddadd/', views.yddadd),
    path('yddquery/', views.yddquery),

    path('dddadd/', views.dddadd),
    path('dddquery/', views.dddquery),
    path('dddupdate/', views.dddupdate),
    path('ddddelete/', views.ddddelete),


]






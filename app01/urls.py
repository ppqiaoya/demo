from django.urls import path
from app01 import views
# from .views import *

urlpatterns = [
    path('ss/', views.ss),

    path('add/',views.add),
    path('query/',views.query),
    path('update/',views.update),
    path('delete/',views.delete),
    path('scx/',views.scx),

    path('yddadd/', views.yddadd),
    path('yddquery/', views.yddquery),
    path('yddupdate/',views.yddupdate),
    path('ydddelete/',views.ydddelete),


    path('dddadd/', views.dddadd),
    path('dddquery/', views.dddquery),
    path('dddupdate/', views.dddupdate),
    path('ddddelete/', views.ddddelete),

    path('jhcx/',views.jhcx),
    path('requesttest/',views.requesttest)



]






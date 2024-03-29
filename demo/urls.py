"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include

from . import views

# from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/', views.hello),
    # re_path(r'^$', views.hello),
    # re_path(r'fenzu/(\d)', views.fenzu),
    # re_path(r'zuming/(?P<year>\d{4})/(?P<city>\w+)', views.zuming),
    # path('gethtml/', views.gethtml),
    #
    path('index/', views.index),
    #
    # path('index2/', views.index2),
    # path('index3/', views.index3),
    # path('xinxi/', views.xinxi),
    # re_path('kongzhi/(\d+)', views.kongzhi),
    # path('staticdemo/',views.staticdemo),

    # path('app01ss/',app01views.ss),

    path('app01/', include('app01.urls')),
]

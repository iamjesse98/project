from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.values, name='values'),
    url(r'^gui/',views.gui,name="gui"),
    url(r'^realtime/', views.rt, name="realTime"),
    url(r'^line/', views.line, name="line")
]

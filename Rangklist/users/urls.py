from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^fractionupload/$', views.fractionupload),
    url(r'^fractionquery/$', views.fractionquery),
]

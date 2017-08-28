"""hcmfront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

from meetings.views import  ReservationDetail, ReservationListView, ReservationCreateView,\
							 ReservationUpdateView, ReservationDeleteView
							

urlpatterns = [
    url(r'^reservation/create/$', ReservationCreateView.as_view(), name='reservation_create'),
    url(r'^reservation/$', ReservationListView.as_view(), name='reservation_list'),
    url(r'^reservation/(?P<pk>[0-9]+)/$', ReservationDetail.as_view(), name='reservation_detail'),
    url(r'^reservation/(?P<pk>[0-9]+)/delete/$', ReservationDeleteView.as_view(), name='reservation_delete'),
    url(r'^reservation/(?P<pk>[0-9]+)/update/$', ReservationUpdateView.as_view(), name='reservation_update'),

    url(r'^admin/', include(admin.site.urls)),
]


from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.home_admission, name='home-admission'),
    url(r'^regisration$', views.registration, name='registration'),
    url(r'^admission$', views.admission, name='admission'),
    url(r'^newAdmission$', views.newAdmission, name='newAdmission'),
    url(r'^newRegistration$', views.new_registration, name='register'),
    url(r'^registration/([0-9]+)/$', views.registration_detail, name='registration-detail'),
    url(r'^registration/edit/(\d+)/$', views.edit, name='edit-registration'),
    url(r'^registration/delete/$', views.delete, name='delete-registration'),
]

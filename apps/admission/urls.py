from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

from . import views

urlpatterns = [
    url(r'^$', views.home_admission, name='home-admission'),
    url(r'^admission$', views.admission, name='admission'), 
    url(r'^newAdmission$', views.new_admission, name='new-admission'),
    # url(r'^admission/confirm$', views.confirm_admission, name='confirm-admission'),
    url(r'^regisration$', views.registration, name='registration'),
    url(r'^newRegistration$', views.new_registration, name='register'),
    url(r'^registration/([0-9]+)/$', views.registration_detail, name='registration-detail'),
    url(r'^registration/edit/(\d+)/$', views.edit_registration, name='edit-registration'),
    url(r'^registration/delete/([0-9]+)$', views.delete_registration, name='delete-registration'),
    url(r'^new-admission-process$', views.new_admission_process, name='new-admission-process'),
    url(r'^admission-process$', views.admission_process, name='admission-process'),
]



# add to the bottom of your file
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
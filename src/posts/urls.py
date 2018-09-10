
from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_detail,
	post_delete,
	post_update
)

urlpatterns = [
    url(r'^create/$', post_create),
    url(r'^detail/$', post_detail),
    url(r'^list/$', post_list),
    url(r'^delete/$', post_delete),
    url(r'^update/$', post_update),

]

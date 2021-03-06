# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'Instanssi.admin_users.views',
    url(r'^$', 'index', name="index"),
    url(r'^users/(?P<su_id>\d+)/delete/', 'delete', name="delete"),
    url(r'^users/(?P<su_id>\d+)/edit/', 'edit', name="edit"),
    url(r'^users/$', 'users', name="users"),
    url(r'^log/$', 'log', name="log"),
)
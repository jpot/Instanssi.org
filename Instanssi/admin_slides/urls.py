# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'Instanssi.admin_slides.views',
    url(r'^$', 'index', name="index"),
    url(r'^slide_entries/(?P<compo_id>\d+)/', 'slide_entries', name="entries"),
    url(r'^slide_results/(?P<compo_id>\d+)/', 'slide_results', name="results"),
)
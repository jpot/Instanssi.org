# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings

# URLS
urlpatterns = patterns('',
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^2012/', include('Instanssi.main2012.urls', namespace="main2012")),
    url(r'^2013/', include('Instanssi.main2013.urls', namespace="main2013")),
    url(r'^2014/', include('Instanssi.main2014.urls', namespace="main2014")),
    url(r'^2015/', include('Instanssi.main2015.urls', namespace="main2015")),
    url(r'^manage/events/', include('Instanssi.admin_events.urls', namespace='manage-events')),
    url(r'^manage/users/', include('Instanssi.admin_users.urls', namespace='manage-users')),
    url(r'^manage/profile/', include('Instanssi.admin_profile.urls', namespace='manage-profile')),
    url(r'^manage/utils/', include('Instanssi.admin_utils.urls', namespace='manage-utils')),
    url(r'^manage/store/', include('Instanssi.admin_store.urls', namespace='manage-store')),
    url(r'^manage/(?P<sel_event_id>\d+)/', include('Instanssi.admin_events_overview.urls', namespace='manage-overview')),
    url(r'^manage/(?P<sel_event_id>\d+)/files/', include('Instanssi.admin_upload.urls', namespace='manage-uploads')),
    url(r'^manage/(?P<sel_event_id>\d+)/blog/', include('Instanssi.admin_blog.urls', namespace='manage-blog')),
    url(r'^manage/(?P<sel_event_id>\d+)/arkisto/', include('Instanssi.admin_arkisto.urls', namespace='manage-arkisto')),
    url(r'^manage/(?P<sel_event_id>\d+)/slides/', include('Instanssi.admin_slides.urls', namespace='manage-slides')),
    url(r'^manage/(?P<sel_event_id>\d+)/screenshow/', include('Instanssi.admin_screenshow.urls', namespace='manage-screenshow')),
    url(r'^manage/(?P<sel_event_id>\d+)/kompomaatti/', include('Instanssi.admin_kompomaatti.urls', namespace='manage-kompomaatti')),
    url(r'^manage/(?P<sel_event_id>\d+)/programme/', include('Instanssi.admin_programme.urls', namespace='manage-programme')),
    url(r'^manage/', include('Instanssi.admin_base.urls', namespace='manage-base')),
    url(r'^api/', include('Instanssi.json_api.urls', namespace="json_api")),
    url(r'^users/', include('Instanssi.users.urls', namespace='users')),
    url(r'^blog/', include('Instanssi.ext_blog.urls', namespace="ext-blog")),
    url(r'^arkisto/', include('Instanssi.arkisto.urls', namespace='archive')),
    url(r'^kompomaatti/', include('Instanssi.kompomaatti.urls', namespace="km")),
    url(r'^screen/', include('Instanssi.screenshow.urls', namespace="screen")),
    url(r'^store/', include('Instanssi.store.urls', namespace='store')),
    url(r'^infodesk/', include('Instanssi.infodesk.urls', namespace='infodesk')),
    url(r'^$', include('Instanssi.main2015.urls')),
)

# Add admin panel link if debug mode is on
if settings.DEBUG or settings.ADMIN:
    from django.contrib import admin
    urlpatterns += patterns('',
        url(r'^admin/', include(admin.site.urls)),
    )

if settings.DEBUG:
    import debug_toolbar

    # Serve media files through static.serve when running in debug mode
    # Also, show debug_toolbar if debugging is on
    urlpatterns += patterns('',
        url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

    # Use admin panel, if debug mode is on
    admin.autodiscover()

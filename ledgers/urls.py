from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',

    url(r'', include('hofuHistoricApp.urls')),
    
    url(r'^ledgers/hofuHistoricApp/', include('hofuHistoricApp.urls')),
)
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()

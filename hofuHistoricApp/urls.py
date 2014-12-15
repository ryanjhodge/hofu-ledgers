from django.conf.urls import patterns, url
from django.views.generic import ListView
from hofuHistoricApp.models import Labordyn
from hofuHistoricApp import views

urlpatterns = patterns('',
                       
    url(r'^$', views.index, name='index'),
    
    url(r'^search/$', views.search, name='search'),

    url(r'^results/$',
        ListView.as_view(
            queryset=Labordyn.objects.all(),
            context_object_name='results_list',
            template_name='hofuHistoricApp/results.html'),
        name='results'),
                       
    url(r'^export/$', views.export, name='export'),
    
    url(r'^certificate/(\d+)/(.+?)$',views.certificate, name='certificate'),
    
    url(r'^pdf/(\d+)/([\w ]+)$', views.pdf, name='pdf'),
    
)

from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from protocol.models import Protocol
from protocol.views import ProtocolDetailView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
            queryset=Protocol.objects.all(),
            context_object_name="protocols_list"),
            name="home"
    ),
    url(r'^protocol/(?P<slug>[a-zA-Z0-9-]+)/$', ProtocolDetailView.as_view(
            queryset=Protocol.objects.all(),
            context_object_name="protocol"),
            name="protocol"
    ),
)

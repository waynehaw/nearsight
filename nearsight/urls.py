"""alerts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from __future__ import absolute_import
from django.conf.urls import url
from . import views
from .signals import handlers  # Signals appear to be unused but they are actually registered with django.

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^nearsight_geojson$', views.geojson),
    url(r'^nearsight_map$', views.viewer),
    url(r'^nearsight_viewer$', views.viewer),
    url(r'^nearsight_upload$', views.upload),
    url(r'^nearsight_layers$', views.layers),
    url(r'^nearsight_layer_download$', views.layer_source_download),
    url(r'^nearsight_status_request$', views.status_request)
]


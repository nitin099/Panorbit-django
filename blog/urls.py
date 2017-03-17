from django.conf.urls import url
from django.contrib import admin
from .views import *
from accounts.views import login_view , register_view , logout_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^(?P<id>\d+)/details/$', details, name='details'),
    url(r'^register/$', register_view, name='register'),
    url(r'^create/$', create, name='create'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^(?P<id>\d+)/update/$', update),
]

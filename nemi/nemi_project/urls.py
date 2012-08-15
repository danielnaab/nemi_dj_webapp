''' Module includes all urls confs for the nemi project '''

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

import methods.urls
import sams.urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {}, name='nemi_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'redirect_field_name' : 'redirect_url'}, name="nemi_logout"),
    url(r'^methods/', include(methods.urls)),
    url(r'^sams/', include(sams.urls)),
    url(r'^home/', TemplateView.as_view(template_name='home.html'), name='home'),
)
"""favorite_places URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

import places.views as places_views
import reg.views as reg_views
import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', places_views.home, name='home'),

    # login/logout
    url(r'^login/$', places_views.login_page, name='login_page'),
    url(r'^logout/$', places_views.logout_page, name='logout_page'),
    url(r'^accounts/logout/$', places_views.logout_page, name='logout_page'),
    url(r'^accounts/login/$', places_views.login_page, name='login_page'),

    # registration
    url(r'^register/$', reg_views.regform, name='regform'),

    # django rest framework urls
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^categories/$', places_views.category_list),
    url(r'^categories/(?P<pk>[0-9]+)/$', places_views.category_detail),
    url(r'^places/(?P<pk>[0-9]+)/$', places_views.place_list),
    url(r'^places/(?P<cat>[0-9]+)/(?P<pid>[0-9]+)/$', places_views.place_detail),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

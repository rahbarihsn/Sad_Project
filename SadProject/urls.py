"""tempProj URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from UserAccount import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^login/$',views.user_login),
    url(r'^register/$',views.register),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$',views.user_logout),
    url(r'register/activate_user/(?P<id>[0-9]+)/$',views.activate_user),
    url(r'^edit_profile/$',views.edit_profile),
    url(r'show_order_work/$',views.show_order_work),
    url(r'^user_account/(?P<username>\w+)/$',views.user_account),
    url(r'add_user/$',views.add_user),
    url(r'sub_works/(?P<name>\w+)/$',views.show_sub_works),
    url(r'^works/$',views.show_works),
    url(r'^workers/(?P<name>\w+)/$',views.show_sub_workers),
    url(r'^logout/$',views.user_logout)

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

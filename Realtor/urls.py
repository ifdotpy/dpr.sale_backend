"""Realtor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin

from .settings import DEBUG, STATIC_URL, MEDIA_ROOT, MEDIA_URL

urlpatterns = [
	url(r'^api/', include('API.urls'))
]

if DEBUG:
	import debug_toolbar

	urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)), )
	urlpatterns += static(STATIC_URL)
	urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

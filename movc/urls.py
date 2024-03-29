"""movc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', include('home.urls')),
    path('maintenance/', include('maintenance.urls')),

    path('about/', include('about.urls')),
    path('people/', include('people.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('contact/', include('contact.urls')),
    path('experience/', include('maintenance.urls')),
    path('apply/', include('apply.urls')),

    prefix_default_language=False,
)

handler404 = lambda request, exception: render(request, '404.html', status=404) 
handler500 = lambda request: render(request, '500.html', status=500) 
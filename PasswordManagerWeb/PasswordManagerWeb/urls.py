"""PasswordManagerWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from core import views
from core.views import CreateSite, DeleteSite, SiteUpdate, HomeListView
from django.conf import settings

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('add/', CreateSite.as_view(), name="add"),
    path('site/<str:pk>/', views.site, name="site"),
    path('update/<int:pk>/', SiteUpdate.as_view(), name="update"),
    path('delete/<int:pk>/', views.DeleteSite.as_view(), name="delete"),
    path('admin/', admin.site.urls),

    # Authentication paths
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""lipid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/'          , admin.site.urls),
    path(''                , views.home, name="home"),
    path('about/'          , views.about, name="about"),
    path('tutorials/'      , views.tutorials, name="tutorials"),
    path('analysis/'       , views.analysis, name="analysis"),
    path('analysis1/'      , views.analysis, name="analysis1"),
    path('analysis2/'      , views.analysis, name="analysis2"),
    path('analysis3/'      , views.analysis, name="analysis3"),
    path('analysis4/'      , views.analysis, name="analysis4"),
    path('analysis5/'      , views.analysis, name="analysis5"),
    path('analysis6/'      , views.analysis, name="analysis6"),
    path('analysis7/'      , views.analysis, name="analysis7"),
    path('analysis8/'      , views.analysis, name="analysis8"),
]

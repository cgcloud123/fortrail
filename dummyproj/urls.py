"""dummyproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from dummyapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexpage, name='indexpage'), 
    # path('ValForm', views.ValForm, name='ValForm'),
    path('contactpage', views.contactpage, name='contactpage'),
    # path('detailform', views.detailform, name='detailform'),

    path('productionpage', views.productionpage, name='productionpage'),
    path('pumppage', views.pumppage, name='pumppage'), 
    path('valvepage', views.valvepage, name='valvepage'), 
    path('CNCpage', views.CNCpage, name='CNCpage'),

    path('pipepage', views.pipepage, name='pipepage'), 
    path('stainlesssteelpage', views.stainlesssteelpage, name='stainlesssteelpage'), 
    path('rubberpage', views.rubberpage, name='rubberpage'), 
    path('gallerypage', views.gallerypage, name='gallerypage'), 

    path('qualitypage', views.qualitypage, name='qualitypage'),
    path('rotterdampage', views.rotterdampage, name='rotterdampage'), 
    path('perfomancepage', views.perfomancepage, name='perfomancepage'), 
    path('life_at_linitpage', views.life_at_linitpage, name='life_at_linitpage'), 
    path('careerspage', views.careerspage, name='careerspage'), 





    # path('linitindex',views.linitindex, name='linitindex'),
]

"""
Desarrollado por Carlos Arteaga, Honduras, Hackathon 2024 SpaceApps NASA
"""

from django.contrib import admin
from django.urls import path
from django.urls import path, include, re_path

#App HomePage URL
from AGROTrace_DEMO.urls import *
#from AGROTrace_DEMO.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AGROTrace_DEMO.urls'), name='homepage'),
    #path('superficieterrestre/',include('AGROTrace_DEMO.urls'), name='superficieterrestre'),
    #path('registro/',include('AGROTrace_DEMO.urls'), name='registro2'),
]

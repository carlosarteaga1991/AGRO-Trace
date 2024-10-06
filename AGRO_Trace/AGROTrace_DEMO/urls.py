from django.contrib import admin
from django.urls import path, include
from AGROTrace_DEMO.views import *

app_name = 'AGROTrace_DEMO'  

urlpatterns = [
    path('',HomePageView.as_view(), name='homepage'),
    #path('SuperficieTerrestre/',DetalleView.as_view(), name='superficieterrestre'),
]
from ensurepip import version
from django.shortcuts import *
from django.views.generic import *
from django.http import *
from datetime import datetime
#from core.HomePage.models import Visita
#from conf.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, DOMAIN
from django.shortcuts import *

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.urls import reverse_lazy

# Para envío de correo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from django.urls import reverse_lazy

# Para mensajes de django
from django.contrib.messages import *


import platform

class HomePageView(TemplateView):
    #model= Visita
    template_name = 'index_DEMO.html'
    error = ""

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['demo'] = 'Demo'
        context['error'] = self.error
        context['login_url']= reverse_lazy('login:iniciar')
        #context['btn_registro'] = reverse_lazy('login:registro')
        #context['politicaPrivacidad_url']= reverse_lazy('HomePage:politicaPrivacidad')

        return context

"""    
class DetalleView(TemplateView):
    #model= Visita
    template_name = 'detalle_DEMO.html'
    error = ""

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['demo'] = 'Demo_detalle'
        context['error'] = self.error
        context['']= reverse_lazy('login:iniciar')
        #context['btn_registro'] = reverse_lazy('login:registro')
        #context['politicaPrivacidad_url']= reverse_lazy('HomePage:politicaPrivacidad')

        return context
"""
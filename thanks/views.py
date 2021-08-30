from django import template
from django.http import request
from django.shortcuts import render
from django.template import Context, Template
from login import views




def thanks(request):
    # getToto = request.session.get("toto")
    # print(getToto)
    # thisToto = "this toto"
    # context = Context({"toto": getToto})
    
    
    #register = template.Library()
    #@register.simple_tag

    return render(request, 'thanks.html')

def getToto():
        
        thisToto = "No name"
        thisToto = request.session.get('toto')
        print("this toto =" ,thisToto)
        return thisToto
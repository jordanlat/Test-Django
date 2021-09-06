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
    
    # thisToto = "No name"
    # thisToto = request.session.get('toto')
    # print("this toto =" ,thisToto)
    thisName = "No name"
    thisName = request.session.get('name')
    print("this name =" ,thisName)
    # getToto(request)
    #register = template.Library()
    #@register.simple_tag

    return render(request, 'thanks.html', {"thisName": thisName})

def getToto(thisrequest):
        thisName = "No name"
        thisName = thisrequest.session.get('toto')
        print("this toto =" ,thisName)
        return thisName
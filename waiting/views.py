from django.http.response import HttpResponse
from django.shortcuts import render

# Mes variables


# Create your views here.
def waiting(request):
    #num = request.session.set
    print("hello you're waiting")

    #return render(request, 'waiting.html')
    return render(request, 'waiting.html')


"""
Marche mais passe par une méthode GET
def counter(request):
    #number= request.session.get("num")
    print("Fock you, stop pressing me")

    return HttpResponse(request,"waiting.html")
"""

def counter(request):
    print("Fock you, stop pressing me")
    return HttpResponse(request,"waiting.html")

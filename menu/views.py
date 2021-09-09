from django.shortcuts import render

# Create your views here.
def menu(request):
    thisNom = request.session.get('nom')
    print("this name = " ,thisNom[0])
    thisPrenom = request.session.get('prenom')
    print("This prenom = ",thisPrenom)
    data = {thisNom, thisPrenom}

    return render(request, 'menu.html', {"nom": thisNom[0], "prenom": thisPrenom})
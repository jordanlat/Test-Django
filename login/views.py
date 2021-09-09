
""""
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

"""""

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from .forms import NameForm



def index(request):
    # if this is a POST request we need to process the form data
    rendered = render_to_string('login.html', {'foo': 'bar'})

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # print(form.cleaned_data['nom'])
            # print(form.cleaned_data['nom'])
            # print(form.cleaned_data['prenom'])
            form_name = form.cleaned_data['nom']
            request.session['nom'] = form_name
            form_prenom = form.cleaned_data['prenom']
            request.session['prenom'] = form_prenom
            # return HttpResponseRedirect('/thanks/')
            return HttpResponseRedirect('/menu/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'login.html', {'form': form})



""""
def index(request):
    # if this is a POST request we need to process the form data
    rendered = render_to_string('login.html')

    return render(request, rendered)
"""""

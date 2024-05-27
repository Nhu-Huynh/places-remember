from django.shortcuts import render, redirect
from .models import Place
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.

def place_page(request, slug):
    place = Place.objects.get(slug=slug)
    return render(request, 'place_page.html', { 'place': place })


@login_required(login_url='/accounts/google/login')
def place_new(request):
    # if this is a POST request we need to process the form data
    # If the form is submitted using a POST request, the view will once again create a form instance and populate it with data from the request: form = CreatePlace(request.POST) This is called “binding data to the form” (it is now a bound form).

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.CreatePlace(request.POST, request.FILES)
        
        # if all fields contain valid data, it will: return True and place the form’s data in its cleaned_data attribute.
        # if it’s not True, we go back to the template with the form. This time the form is no longer empty (unbound) so the HTML form will be populated with the data previously submitted, where it can be edited and corrected as required.

        if form.is_valid():
            # save with user 
            newPlace = form.save(commit=False)
            newPlace.author = request.user
            newPlace.save()
            return redirect('/') 
    else:
        # If we arrive at this view with a GET request, it will create an empty form instance and place it in the template context to be rendered. This is what we can expect to happen the first time we visit the URL.

        form  = forms.CreatePlace()
    
    return render(request, 'place_new.html', { 'form': form })

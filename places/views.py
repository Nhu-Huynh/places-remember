from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import PlaceForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/')
def place_new_view(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            # save with user 
            newPlace = form.save(commit=False)
            newPlace.author = request.user
            newPlace.save()
            return redirect('/') 
    else:
        form  = PlaceForm()
    
    return render(request, 'place_new.html', { 'form': form })


@login_required(login_url='/')
def place_update_view(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    if request.method == 'POST':
        form = PlaceForm(request.POST, instance=place)
        if form.is_valid():
            form.save()
            return redirect('users:home')
    else:
        form = PlaceForm(instance=place)
    
    return render(request, 'place_new.html', { 'form': form, 'update': True })


@login_required(login_url='/')
def place_delete_view(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    if request.method == 'POST':
        place.delete()
        return redirect('users:home')
    else:
        return render(request, 'place_confirm_delete.html', { 'place': place })

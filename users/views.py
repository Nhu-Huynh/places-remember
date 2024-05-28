from django.shortcuts import render, redirect
from django.contrib.auth import logout
from places.models import Place

# Create your views here.

def home(request):   
    places = Place.objects.all().order_by('-date')

    places = Place.objects.raw('SELECT * FROM places_place WHERE author_id = %s ORDER BY date DESC', [request.user.id])

    # print(places)

    if request.user.is_authenticated:
        print('user authenticated')
        # print(request.user.id)
        return render(request, 'home.html', { 'places': places })
    else:
        print('no user')
        return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect('/')

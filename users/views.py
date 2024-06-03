from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from places.models import Place

# Create your views here.


def home(request):
    if not request.user.is_authenticated:
        return redirect("/")

    place_list = Place.objects.filter(author=request.user).order_by("-date")
    paginator = Paginator(place_list, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "home.html", {"page_obj": page_obj})


def logout_view(request):
    logout(request)
    return redirect("/")

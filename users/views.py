from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from places.models import Place

# Create your views here.


def home(request):
    # places = Place.objects.all().order_by("-date")

    place_list = Place.objects.raw(
        "SELECT * FROM places_place WHERE author_id = %s ORDER BY date DESC",
        [request.user.id],
    )

    # print(places)

    paginator = Paginator(place_list, 2)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "home.html", {"page_obj": page_obj})

    # if request.user.is_authenticated:
    #     print("user authenticated")
    #     # print(request.user.id)
    #     return render(request, "home.html", {"places": places})
    # else:
    #     print("no user")
    #     return render(request, "home.html")


def logout_view(request):
    logout(request)
    return redirect("/")

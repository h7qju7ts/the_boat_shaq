from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Boat

# Create your views here.

def home(request):
    return render(request, "home/home.html")

def boat_detail(request, slug):
    boat = get_object_or_404(Boat, slug=slug)
    return render(request, "boats/boat_detail.html", {"boat": boat})

@login_required
def profile(request):
    return render(request, "profile/profile.html")

def catalog(request):
    qs = Boat.objects.all()

    q = request.GET.get("q", "").strip()
    if q:
        qs = qs.filter(
            Q(name__icontains=q) |
            Q(short_description__icontains=q) |
            Q(description__icontains=q) |
            Q(brand__name__icontains=q) |       
            Q(category__name__icontains=q)
        ).distinct()

    sort = request.GET.get("sort", "")
    if sort == "price_asc":
        qs = qs.order_by("price")
    elif sort == "price_desc":
        qs = qs.order_by("-price")
    elif sort == "newest":
        qs = qs.order_by("-created_at")  # or "-id" if you don't have created_at
    elif sort == "name":
        qs = qs.order_by("name")

    paginator = Paginator(qs, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "boats/catalog.html", {
        "boats": page_obj.object_list,
        "page_obj": page_obj,
    })
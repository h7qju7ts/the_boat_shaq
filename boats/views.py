from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Boat, Category

def home(request):
    return render(request, "home/home.html")

def boat_detail(request, slug):
    boat = get_object_or_404(Boat, slug=slug)
    return render(request, "boats/boat_detail.html", {"boat": boat})

@login_required
def profile(request):
    return render(request, "profile/profile.html")

def catalog(request):
    qs = Boat.objects.filter(is_available=True).select_related("brand", "category")

    q = request.GET.get("q", "").strip()
    if q:
        qs = qs.filter(
            Q(name__icontains=q) |
            Q(short_description__icontains=q) |
            Q(description__icontains=q) |
            Q(brand__name__icontains=q) |
            Q(category__name__icontains=q)
        ).distinct()

    category_slug = request.GET.get("category", "").strip()
    if category_slug:
        qs = qs.filter(category__slug=category_slug)

    sort = request.GET.get("sort", "")
    if sort == "price_asc":
        qs = qs.order_by("price")
    elif sort == "price_desc":
        qs = qs.order_by("-price")
    elif sort == "newest":
        qs = qs.order_by("-created_at")
    elif sort == "name":
        qs = qs.order_by("name")
    else:
        qs = qs.order_by("-created_at")

    paginator = Paginator(qs, 12)
    page_obj = paginator.get_page(request.GET.get("page"))

    categories = Category.objects.all().order_by("name")

    return render(request, "boats/catalog.html", {
        "boats": page_obj.object_list,
        "page_obj": page_obj,
        "categories": categories,
    })
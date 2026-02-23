from django.shortcuts import render

# Create your views here.
def basket_view(request):
    return render(request, "basket/basket.html")
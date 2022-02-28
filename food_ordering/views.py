from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.urls import reverse
from django.utils.text import slugify

resturants = Resturant.objects.all().order_by('user_id__address__city')

cities = []
city_objects = []

for r in resturants:
    city = r.user_id.address.city
    if cities.count(city) == 0:
        cities.append(city)

for city in cities:
    city_count = Resturant.objects.filter(user_id__address__city = city).count()
    city_objects.append({
        'city_name': city, 
        'count': city_count,
        'city_url': slugify(city)
    })

# Create your views here.
def show_resturants(request):
    return render(request, 'food_ordering/resturants.html', {
        'resturants': resturants,
        'cities': city_objects
    })

def show_resturants_by_city(request, slug):
    city = str(slug).replace('-', ' ').capitalize()
    city_resturants = Resturant.objects.filter(user_id__address__city = city)

    return render(request, 'food_ordering/city_resturants.html', {
        'city': str(slug),
        'resturants': city_resturants
    })

def show_single_resturant(request, slug):
    resturant = Resturant.objects.get(slug = slug)
    return render(request, 'food_ordering/single_resturant.html', {
        'resturant': resturant,
        'menu': resturant.foods.all(),
        'comments': resturant.comments.all()
    })

def show_menu_item(request, slug, id):
    return HttpResponse('Menu Item')

def show_comments(request, slug):
    return HttpResponse('Comments')
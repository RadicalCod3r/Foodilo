from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('resturant/', views.show_resturants),
    path('resturant/city/<slug:slug>', views.show_resturants_by_city, name='by_city'),
    path('resturant/<slug:slug>', views.show_single_resturant, name='single_resturant'),
    path('resturant/<slug:slug>/menu/<int:id>', views.show_menu_item),
    path('resturant/<slug:slug>/comments', views.show_comments)
]
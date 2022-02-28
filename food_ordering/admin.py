from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_url', 'rating')

class AccountAdmin(admin.ModelAdmin):
    list_display = ('acc_number', 'bank_id')

class ResturantAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('resturant_name',)}

admin.site.register(Bank)
admin.site.register(User, UserAdmin)
admin.site.register(Account)
admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(Resturant, ResturantAdmin)
admin.site.register(Customer)
admin.site.register(Courier)
admin.site.register(Comment)
admin.site.register(Motorcycle)
admin.site.register(Food, FoodAdmin)
admin.site.register(Order)
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=50, null=False, unique=True)
    email = models.CharField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.email

class Account(models.Model):
    acc_number = models.CharField(max_length=10)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=False, related_name='accounts')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='accounts')

    def __str__(self):
        return self.acc_number

class Address(models.Model):
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=False, related_name='address')

    def __str__(self):
        return f'{self.street}, {self.city}, {self.country}'

    class Meta:
        verbose_name_plural = 'Addresses'

class Phone(models.Model):
    phone_number = models.CharField(max_length=10)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.phone_number

class Resturant(models.Model):
    resturant_name = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    slug = models.SlugField(default='')

    def get_absolute_url(self):
        return reverse('single_resturant', args=[self.slug])
    

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.resturant_name)}-{slugify(self.user_id.address.street)}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.resturant_name

class Customer(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.user_id.username

class Courier(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.user_id.username

class Comment(models.Model):
    resturant_id = models.ForeignKey(Resturant, on_delete=models.CASCADE, null=False, related_name='comments')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, related_name='comments')
    comment_text = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'Customer: {self.customer_id.user_id.username}, Resturant: {self.resturant_id.resturant_name}'

class Motorcycle(models.Model):
    courier_id = models.OneToOneField(Courier, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)

class Food(models.Model):
    name = models.CharField(max_length=20)
    image_url = models.TextField()
    resturant_id = models.ForeignKey(Resturant, on_delete=models.CASCADE, null=False, related_name='foods')
    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.name}, {self.resturant_id.resturant_name}'
   
class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE, null=False)
    courier_id = models.ForeignKey(Courier, on_delete=models.CASCADE, null=False)
    date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.food_id.resturant_id.resturant_name} ({self.food_id.resturant_id.user_id.address.street}) To {self.customer_id.user_id.address.street}'
    
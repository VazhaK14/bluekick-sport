import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import *
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    CATEGORY_CHOICHES = [
        ('ball', 'Ball'), 
        ('accessory', 'Accessory'), 
        ('socks', 'Socks'), 
        ('shoes', 'Shoes'), 
        ('jersey', 'Jersey'),
        ('training set', 'Training Set')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICHES, default='ball')
    rating = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    rating_sum = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)
    is_avail = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    @property
    def is_product_top(self):
        return self.rating > 3
    
    def save(self, *args, **kwargs):
        self.is_avail = self.stock > 0
        super().save(*args, **kwargs)
    
    def give_rating(self, rate):
        if rate < 0 or rate > 5:
            raise ValueError('Rating Product is 0-5')
        
        self.rating_sum += rate
        self.rating_count += 1

        self.rating = min(self.rating_sum / self.rating_count, 5)
        return self.rating
    
class Seller(models.Model):
    name = models.CharField(max_length=255)
    birthdate = models.DateField()
    telp_number = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    is_active = models.BooleanField(default=False)
    social_medias = ArrayField(models.URLField(blank=True, null=True), default=list, blank=True)


    
    

import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICHES = [
        ('ball', 'Ball'), 
        ('accessory', 'Accessory'), 
        ('socks', 'Socks'), 
        ('shoes', 'Shoes'), 
        ('jersey', 'Jersey'),
        ('training set', 'Training Set')
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICHES, default='update')
    rating = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    rating_sum = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)
    is_avail = models.BooleanField(default=False)
    
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
        self.save()
        return self.rating


    
    

from django.forms import *
from main.models import *

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'description', 'thumbnail', 'category', 'is_featured']

class SellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'birthdate', 'telp_number', 'email', 'address', 'is_active', 'social_medias']
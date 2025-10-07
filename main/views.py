import datetime
from django.shortcuts import *
from main.models import Product
from main.forms import *
from django.core import serializers

from django.http import *
from django.urls import *
from django.core import serializers

from django.contrib.auth.forms import *
from django.contrib import messages
from django.contrib.auth import *
from django.contrib.auth.decorators import *

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    seller_list = Seller.objects.all()

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'app_name': 'BlueKick Sport',
        'name': request.user.username,
        'class': 'PBP-F',
        'product_list': product_list,
        'seller_list': seller_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    # Handle AJAX requests for product refresh
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        from django.template.loader import render_to_string
        # Render only the products section for AJAX requests
        products_context = {
            'product_list': product_list,
            'user': request.user,
            'name': request.user.username,
            'app_name': 'BlueKick Sport'
        }
        products_html = render_to_string('products_section.html', products_context, request)

        return JsonResponse({
            'success': True,
            'products_html': products_html,
            'product_count': len(product_list)
        })

    return render(request, 'main.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            if form.is_valid():
                product_entry = form.save(commit=False)
                product_entry.user = request.user
                product_entry.save()
                return JsonResponse({"success": True, "redirect_url": "/"})
            else:
                return JsonResponse({"success": False, "error": "Invalid form data."})
        else:
            if form.is_valid():
                product_entry = form.save(commit=False)
                product_entry.user = request.user
                product_entry.save()
                return redirect('main:show_main')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'add_product.html', context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == "POST":
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            rate = int(request.POST.get('rate', 0))
            product.give_rating(rate)
            product.stock -= 1
            product.save()
            return JsonResponse({"success": True, "redirect_url": "/"})
        else:
            rate = int(request.POST.get('rate', 0))
            product.give_rating(rate)
            product.stock -= 1
            product.save()
            return redirect('main:show_main')

    context = {'product': product}
    return render(request, 'product_detail.html', context)

def add_seller(request):
    form = SellerForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        seller_entry = form.save(commit=False)
        seller_entry.user = request.user
        seller_entry.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, 'add_seller.html', context)
    

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            if form.is_valid():
                form.save()
                return JsonResponse({"success": True, "redirect_url": "/"})
            else:
                return JsonResponse({"success": False, "error": "Invalid form data."})
        else:
            if form.is_valid():
                form.save()
                return redirect('main:show_main')
    else:
        form = ProductForm(instance=product)
    context = {'form': form}
    return render(request, 'edit_product.html', context)


def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
        product.delete()
        return JsonResponse({"success": True, "message": "Product deleted successfully."})
    elif request.method == "GET":
        # Fallback for GET requests (though we should use POST)
        product.delete()
        return JsonResponse({"success": True, "message": "Product deleted successfully."})
    else:
        product.delete()
        return HttpResponseRedirect(reverse('main:show_main'))


def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize('xml', product_list)
    return HttpResponse(xml_data, content_type='application/xml')


def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize('json', product_list)
    return HttpResponse(json_data, content_type='application/json')


def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize('xml', product_item)
        return HttpResponse(xml_data, content_type='application/xml')
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product_item = Product.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [product_item])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            if form.is_valid():
                user = form.save()
                return JsonResponse({
                    "success": True,
                    "redirect_url": "/login",
                    "message": "Account created successfully! Please log in."
                })
            else:
                return JsonResponse({
                    "success": False,
                    "error": "Registration failed. Please check your input."
                })
        else:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
            else:
                messages.error(request, 'Registration failed. Please check your input.')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            if user is not None:
                login(request, user)
                response = JsonResponse({
                    "success": True,
                    "redirect_url": "/",
                    "message": f"Welcome back, {user.username}!"
                })
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                return JsonResponse({
                    "success": False,
                    "error": "Invalid username or password"
                })
        else:
            # Handle normal form submission
            if user is not None:
                login(request, user)
                response = redirect('main:show_main')
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                messages.error(request, 'Invalid username or password')
                return render(request, 'login.html')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response





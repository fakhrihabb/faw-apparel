import json

from django.shortcuts import render, redirect
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_mood = Product.objects.create(
            user=request.user,
            name=data["name"],
            price=int(data["price"]),
            description=data["description"]
        )

        new_mood.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
          user = form.get_user()
          login(request, user)
          response = HttpResponseRedirect(reverse('main:show_main'))
          response.set_cookie('last_login', str(datetime.datetime.now()))
          return response
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:show_main'))
    response.delete_cookie('last_login')
    return response

@login_required
def get_user_products(request):
    try:
        if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Ensure it's an AJAX GET request
            user = request.user
            print(f"User: {user}")
            # Filter products based on the logged-in user (adjust this depending on your product model)
            products = Product.objects.filter(user=user)  # Assuming Product has a foreign key to user
            product_list = list(products.values())  # Convert queryset to a list of dicts
            return JsonResponse({'products': product_list}, status=200)
        return JsonResponse({'error': 'Invalid request'}, status=400)
    except Exception as e:
        # DEBUG: Print the exact error in the server logs
        print(f"Error: {e}")
        return JsonResponse({'error': str(e)}, status=500)

@login_required(login_url='/login')
def show_main(request):
    # product = Product.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'app_name': 'FawApparel',
        'class': 'PBP C',
        # 'products': product,
        'last_login': request.COOKIES.get('last_login'),
    }

    return render(request, 'main.html', context)

@csrf_exempt
@require_POST
def create_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    user = request.user

    new_product = Product(name=name, price=price, description=description, user=user)
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')
    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def edit_product(request, id):
    product = Product.objects.get(pk=id)
    form = ProductEntryForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def clean_name(self):
    name = self.cleaned_data["name"]
    return strip_tags(name)

def clean_description(self):
    description = self.cleaned_data["description"]
    return strip_tags(description)

from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import Product
def show_main(request):
    product_entries = Product.objects.all()
    context = {
        'app_name': 'FawApparel',
        'name': 'Fakhri',
        'class': 'PBP C',
        'product_entries': product_entries,
    }

    return render(request, 'main.html', context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
# Create your views here.

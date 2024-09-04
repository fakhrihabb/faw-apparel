from django.shortcuts import render
def show_main(request):
    context = {
        'app_name': 'FawApparel',
        'name': 'Fakhri',
        'class': 'PBP C',
    }

    return render(request, 'main.html', context)
# Create your views here.

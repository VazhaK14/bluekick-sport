from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name': 'BlueKick Sport',
        'name': 'Vazha Khayri',
        'class': 'PBP-F'
    }

    return render(request, 'main.html', context)
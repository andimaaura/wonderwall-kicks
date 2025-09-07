from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'app_title' : 'Wonderwall Kicks',
        'user_name': 'Andi Maura Azzahra',
        'user_class' : 'PBP C',
        'npm' : '2406409076'
       
    }

    return render(request, 'main.html', context)
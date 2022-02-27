from django.shortcuts import render
from .models import Photo

# Create your views here.
def home(request):
    context = {
        'pics': Photo.objects.all()
    }
    return render(request, 'photos/home.html', context)
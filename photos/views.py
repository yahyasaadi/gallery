from django.shortcuts import render
from django.db.models import Q
from .models import Photo, Location, Category

# Create your views here.
def home(request):
    context = {
        'pics': Photo.objects.all()
    }
    return render(request, 'photos/home.html', context)


# Search method
def search(request):
	if request.method == "POST":
		searched = request.POST['searched']
		pics = Photo.objects.filter(img_category__img_category__contains=searched)
	
		return render(request, 'photos/search.html', {'searched':searched, 'pics':pics})
	else:
		return render(request, 'photos/search.html')

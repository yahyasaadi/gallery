from django.shortcuts import render
from .models import Photo, Location, Category

# Create your views here.
def home(request):
    context = {
        'pics': Photo.objects.all()
    }
    return render(request, 'photos/home.html', context)


# Search method
def search(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Photo.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"req_images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})
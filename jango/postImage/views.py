from django.shortcuts import render

from .models import PostImage
def rumah(request):
    context = {
        'imej' : PostImage.objects.all()
    }
    return render(request, 'postimage/home.html', context)

def tentang(request):
    return render(request, 'postimage/about.html')
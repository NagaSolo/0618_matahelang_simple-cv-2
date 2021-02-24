from django.shortcuts import render

from .models import PostImage

from django.views.generic import ListView, DetailView

# Ini sudah tidak diguna
def rumah(request):
    context = {
        'imej' : PostImage.objects.all()
    }
    return render(request, 'postimage/home.html', context)

# gunapakai kelas ListView
class ImejListView(ListView):
    model = PostImage
    template_name = 'postimage/home.html'
    context_object_name = 'imej'
    ordering = ['-date_posted'] # order imej in latest updated

# gunapakai kelas DetailView untuk detail setiap post imej
class ImejDetailView(DetailView):
    model = PostImage

def tentang(request):
    return render(request, 'postimage/about.html')
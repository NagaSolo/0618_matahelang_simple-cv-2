from django.shortcuts import render

from .models import PostImage

from django.views.generic import (
    ListView, 
    DetailView,
    CreateView
)

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

# gunapakai kelas CreateView untuk post imej baharu
class ImejCreateView(CreateView):
    model = PostImage
    fields = ['title', 'content', 'cover']

    def form_valid(self, form):
        # check if owner of the form sent is the same as currently logged in user
        form.instance.owner == self.request.user
        return super().form_valid(form)

def tentang(request):
    return render(request, 'postimage/about.html')
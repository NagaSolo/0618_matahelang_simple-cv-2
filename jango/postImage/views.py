from django.shortcuts import render

from .models import PostImage

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
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
    template_name = 'postimage/post_detail.html'

# gunapakai kelas CreateView untuk post imej baharu
class ImejCreateView(LoginRequiredMixin, CreateView):
    model = PostImage
    template_name = 'postimage/post_form.html'
    fields = ['title', 'content', 'cover']

    def form_valid(self, form):
        # check if owner of the form sent is the same as currently logged in user
        form.instance.owner == self.request.user
        return super().form_valid(form)

# gunapakai kelas UpdateView untuk update post
class ImejUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostImage
    template_name = 'postimage/post_form.html'
    fields = ['title', 'content', 'cover']

    def form_valid(self, form):
        # check if owner of the form sent is the same as currently logged in user
        form.instance.owner == self.request.user
        return super().form_valid(form)

    def test_func(self):
        imej = self.get_object()
        if self.request.user == self.imej.owner:
            return True
        return False

# gunapakai kelas DeleteView untuk delete setiap spesifik imej
class ImejDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostImage
    success_url = '/'

    def test_func(self):
        imej = self.get_object()
        if self.request.user == self.imej.owner:
            return True
        return False

def tentang(request):
    return render(request, 'postimage/about.html')
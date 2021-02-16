from django.shortcuts import render

def rumah(request):
    return render(request, 'postimage/home.html')

def tentang(request):
    return render(request, 'postimage/about.html')
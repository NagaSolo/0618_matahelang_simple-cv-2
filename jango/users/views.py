from django.shortcuts import render, redirect

# import user registration form from forms.py
from .forms import UserRegisterForm

# guna decorator untuk restrict access ke page
from django.contrib.auth.decorators import login_required

from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # simpan valid form
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akaun {username} berjaya dicipta')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
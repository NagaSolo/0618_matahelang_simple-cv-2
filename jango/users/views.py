from django.shortcuts import render

# import user registration form from forms.py
from .forms import UserRegisterForm

from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid:
            form.save() # simpan valid form
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akaun {username} berjaya dicipta')
            return redirect('postImage-rumah')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})
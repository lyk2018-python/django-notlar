from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email=form.cleaned_data.get('email')
            user = authenticate(username=username,password=raw_password,email=email)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})
      
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def support(request):
    return render(request, 'support.html')
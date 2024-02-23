from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, LoginForm, SignupForm
from .models import Userprofile
from django.contrib.auth.models import User

# Create your views here.

# Home page
#@login_required
def index(request):
        return render(request, 'index.html')

#member list page    
@login_required   
def member_list(request):
    full_name = request.user.userprofile.get_full_name()
    users = Userprofile.objects.exclude(user=request.user)
    return render(request, 'member_list.html', {'full_name': full_name, 'users': users})    

#profile page    
@login_required 
def view_profile(request, username):
    user_profile = get_object_or_404(Userprofile, user__username=username)
    return render(request, 'view_profile.html', {'user_profile': user_profile})
  

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})



# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('member_list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout 
def user_logout(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,aauthenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegForm

def register_wiew(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("my_entries")
    else:
            return render(request, "users/register.html", {"form": form})

def login_wiev(request):
    if request.method == 'POST':
          form = AuthenticationForm(request,data = request.POST)
          if form.is_valid():
               login(request,form.get_user())
               return redirect("my_entries")
    else:
        return render(request, "users/login.html", {"form": form})


def logout_wiew(request):
     logout(request)
     return redirect('home_page')
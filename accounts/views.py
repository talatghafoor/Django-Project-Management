from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.views import LoginView
from projects import urls

# Create your views here.
def registration(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # return redirect('home')
    form = UserCreationForm
    context = {'form':form}
    return render(request, 'users/registration.html', context)




class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form = AuthenticationForm


def logout_user(request):
   logout(request)
   return redirect("login")
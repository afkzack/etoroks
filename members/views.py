from django.views import generic
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Username OR Password is incorrect.")
        
    context = {}
    return render(request, 'members/login.html', context)
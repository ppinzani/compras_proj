from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from .forms import LoginForm


# Create your views here.
def userlogin(request):
    if request.method == "POST":
        if 'login_form' in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('/proveedores')
        else:
            login_form = LoginForm()
            return redirect('/')
    else:
            login_form = LoginForm()

    template = 'usuarios/login.html'
    variables = {'login_form': login_form}

    return render(request, template, variables)

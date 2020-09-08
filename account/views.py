from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # Instatiating the from 
        if form.is_valid():
            #Check the validity of the form 
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            #If the data is valid then check against the database to see if they are a valid user
            if user is not None: 
                if user.is_active:
                    #Check if the user is active 
                    login(request,user)
                    return HttpResponse('Authenticaated')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

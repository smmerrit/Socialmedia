from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
#from .models import Profile

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})



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


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data.get("password"))
            # Save the User object
            new_user.save()
            # Create the user profile
         #   Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})

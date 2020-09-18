from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreationForm

@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreationForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image Added')
        else:
            form = ImageCreationForm(data=request.GET)
        return render('images/image/create.html',{'section': 'images', 'form': form})


# Create your views here.

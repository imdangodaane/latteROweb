from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .forms import SignupForm

# Create your views here.
def mainpage(request):
    """Signup view"""
    if request.method == 'POST':
        # Get signup form from template
        form = SignupForm(request.POST)
        if form.is_valid():
            # Valid form then save
            form.save()
            # return render(request, 'mainpage/signup_success.html')
            return HttpResponse("Sign up success.")
        else:
            return render(request, 'mainpage/mainpage.html', {'form': form,})
    else:
        # Send signup form to template
        form = SignupForm()
    return render(request, 'mainpage/mainpage.html', {'form': form})

def signup(request):
    """Signup view"""
    if request.method == 'POST':
        # Get signup form from template
        form = SignupForm(request.POST)
        if form.is_valid():
            # Valid form then save
            form.save()
            # return render(request, 'mainpage/signup_success.html')
            return HttpResponse("Sign up success.")
        else:
            return render(request, 'mainpage/mainpage.html', {'form': form,})
    else:
        # Send signup form to template
        form = SignupForm()
    return render(request, 'mainpage/mainpage.html', {'form': form})

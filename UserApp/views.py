from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Welcome, {username}")
            return redirect("platform-home")
    else:
        form = UserRegistrationForm()
    
    return render(request, "UserApp/registration.html", { "form": form })
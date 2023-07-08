from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm




def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            logout(request)
            user = form.save(commit=False)  # Create user object without saving
            user.is_staff = False  # Set is_staff attribute to False
            form.save()  # Save the user object
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Account successfully created!")
            return redirect('/account/login')

    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form})

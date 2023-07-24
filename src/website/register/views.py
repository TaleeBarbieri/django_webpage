from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.models import User



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

def reset_password(request):
    if request.method == "POST":
        username = request.POST.get('username')
        raw_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not raw_password or not confirm_password:
            messages.error(request, "Please provide both username and new password.")
            return render(request, "reset_password.html")

        if raw_password != confirm_password:
            messages.error(request, "New passwords do not match.")
            return render(request, "reset_password.html")

        try:
            user = User.objects.get(username=username)
            user.set_password(raw_password)
            user.save()
            messages.success(request, "Password successfully reset. You can now log in with the new password.")
            return redirect('/account/login')

        except User.DoesNotExist:
            messages.error(request, "User with the provided username does not exist.")
            return render(request, "reset_password.html")

    return render(request, "reset_password.html")

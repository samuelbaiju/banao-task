
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm
# Create your views here.
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect('login')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            selected_role = form.cleaned_data['role']

            user = authenticate(username=username, password=password)
            if user:
                if user.role == selected_role:
                    login(request, user)
                    if selected_role == 'doctor':
                        return redirect('doctor_dashboard')
                    else:
                        return redirect('patient_dashboard')
                else:
                    messages.error(
                        request,
                        f"There is no account with this credentials in {selected_role}'."
                    )
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html', {'user': request.user})

@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')

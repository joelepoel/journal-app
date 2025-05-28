from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserForm, CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('entry_list') #Redirects to journal entry list page
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

    
@login_required
def account_details(request):
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile') #Redirects to profile page
    else:
        form = UserForm(instance=request.user, user=request.user)

    return render(request, 'accounts/account_details.html', {'form': form})
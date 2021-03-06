from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.


def register(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save(*args, **kwargs)
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You can now login!')
            # * redirecting to the blog homepage, using the name given for the url pattern of blog homepage.
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request, *args, **kwargs):
    if request.method == 'POST':
        # here instance is basically setting the default input into the fields.
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save(*args, **kwargs)
            p_form.save(*args, **kwargs)
            messages.success(
                request, f'Your account has been updated, mate!')
            # * redirecting to the blog homepage, using the name given for the url pattern of blog homepage.
            return redirect('blog-home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

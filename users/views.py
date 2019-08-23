from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfilUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Votre compte a ete cree avec success {username}')
            return redirect('profil')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, "users/register.html", context)

@login_required
def profil(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST)
        p_form = ProfilUpdateForm(request.POST)
    else:
        u_form = UserUpdateForm()
        p_form = ProfilUpdateForm()

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, "users/profil.html", context)


@login_required
def profil_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfilUpdateForm(request.POST, request.FILES, instance=request.user.profil)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Votre compte a ete modifie avec success')
            return redirect('profil')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilUpdateForm(instance=request.user.profil)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, "users/profil_update.html", context)
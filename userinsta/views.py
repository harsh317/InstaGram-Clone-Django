from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterExtra,UserupdateForm,ProfileUpdateForm
from .models import ProfilePic
# Create your views here.

def registerInsta(request):
    if request.method == 'POST':
        form = UserRegisterExtra(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,'Your Account Had Been Created!.Now you can Log In')
            return redirect('login')
    else:
        form = UserRegisterExtra()
    return render(request,'users/register.html',context={'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserupdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profilepic)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserupdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilepic)
    return render(request,'users/profile.html',{'u_form':u_form,'p_form':p_form})


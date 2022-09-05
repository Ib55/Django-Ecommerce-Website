from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from App_Login.forms import ProfileForm,SignUpForm
# Create your views here.
from App_Login.models import  Profile


from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def Sign_up(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Account Create Successfully')
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request,'App_Login/signup.html',context={'form':form,'title':'Signup Page'})



def Login_Page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('App_Shop:home'))
    return render(request,'App_Login/login.html',context={'form':form,'title':'Login Page'})


@login_required
def Logout_Page(request):
    logout(request)
    messages.warning(request,'You are logged out!!')
    return HttpResponseRedirect(reverse('App_Login:login'))

@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Account Update Successfully')
            form = ProfileForm(instance=profile)
    return render(request,'App_Login/change_profile.html',context={'form':form,'title':'Change Profile'})
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,get_user_model
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {
        "title":"Home page"
    }
    if request.user.is_authenticated:
        context['p_content'] = "hello vivek"
    return render(request, 'home.html',context)


def about(request):
    context = {
        "about":"about page"
    }

    return render(request, 'about.html', context)

def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "contact":"contact page",
        "form":contact_form,
        "brand":"new brand"
    }
    
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST.get("fullname"))
    #     print(request.POST.get("email"))
    #     print(request.POST.get("password"))
    #     print(request.POST.get("content"))

    return render(request, 'contact/view.html',context)


def loginuser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    print("user loggedIn")
    #print(request.user.is_authenticated)    
    if form.is_valid():
        print(form.cleaned_data)
        
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #print(request.user.is_authenticated)
            login(request, user)
            #contenxt['form'] = LoginForm()
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            print("error")
        
    return render(request, 'auth/login.html',   context)



User  = get_user_model()
def registration(request):
    form = RegisterForm(request.POST or None)
    context ={
        "register":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email    = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
       
        new_user = User.objects.create_user(username,email, password)
        print(new_user)
        
    return render(request, 'auth/register.html', context)
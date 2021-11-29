from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

# Create your views here.

def home_page(request):
    return render(request, "website.html", {"title":"Home"})

def signIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            name = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            return render(request, "users/login_success.html",{"name":name})
        else:
            messages.error(request, "The user dosen't exist, Please sign up or try again!!")
            return redirect('loginfailed')

    return render(request, "users/Loginpage.html")


def signUp(request):

    if request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        adress = request.POST.get('adress')
        password = request.POST.get('password')
        
        # if len(password)<8:
        #     messages.error(request, "Username must be under 20 charcters!!")
        #     return redirect('home')
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = name
        myuser.last_name = lastName
        # myuser.is_active = False
        myuser.save()
        
        # # Welcome Email
        # subject = "Welcome to pet-protected Login!!"
        # message = "Hello " + myuser.first_name + "! \n" + "Welcome to pet-protected! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You"
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # # Email Address Confirmation Email
        # current_site = get_current_site(request)
        # email_subject = "Confirm your Email @ pet-protected Login!!"
        # message2 = render_to_string('email_confirmation.html',{
            
        #     'name': myuser.first_name,
        #     'domain': current_site.domain,
        #     'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        #     'token': generate_token.make_token(myuser)
        # })
        # email = EmailMessage(
        # email_subject,
        # message2,
        # settings.EMAIL_HOST_USER,
        # [myuser.email],
        # )
        # email.fail_silently = True
        # email.send()
        
        return redirect('signin')
        
    return render(request, "users/SignUp.html")


def loginDetails(request):
    return render(request, "users/login_details.html", {"title":"Login Details"})

def add_post(request):
    return render(request, "AddAd.html", {"title":"Add a post"})

def add_review(request):
    return render(request, "AddReview.html", {"title":"Add a review"})

def posts(request):
    return render(request, "Home.html", {"title":"Posts"})

def login_failed(request):
    return render(request, "users/login_failed.html", {"title":"Login failed"})

def login_success(request):
    return render(request, "users/login_success.html", {"title":"Login success"})

def signOut(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')
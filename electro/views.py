from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from electro.models import customer_request,customer_message,subscriber,review
from .forms import register,message,bookForm,update_profile,profile_pic_update,c_reviews
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    if request.method=='POST':
        form=message(request.POST)
        if form.is_valid() or rev.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('/')

    rev = c_reviews()
    revs=review.objects.all()
    form = message()
    forms=customer_message.objects.all()
    context={'form':form,'forms':forms,'rev':rev,'revs':revs}
    return render(request,'index.html',context)

def logins(request):

    if request.method=="POST":
        username=request.POST.get('names')
        password=request.POST.get('pass')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Username Or Password Is Incorrect')
            return redirect('logins')

    return render(request,'logins.html')
    
def reg(request):
    if request.method == "POST":
        form=register(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account has been created for '+user)
            return redirect('logins')
        else:
            messages.error(request, form.errors.get('username'))
    form = register()
    context={'form':form}
    return render(request,'reg.html',context)

def logoutuser(request):
    logout(request)
    return redirect('home')

def subscrib(request):
    if request.method == "POST":
        email = request.POST.get('email')
        sub = subscriber(email_ID=email)
        sub.save()
    return redirect('/')

@login_required(login_url="/logins")
def booking(request):
    if request.method=='POST':
        form=bookForm(request.POST)
        if form.is_valid():
            update=form.save(commit=False)
            update.connect=request.user
            update.save()

    form = bookForm()
    context={'form':form}
    return render(request,'bookings.html', context)

class PasswordsChangeView(SuccessMessageMixin,PasswordChangeView):
    form_class=PasswordChangeForm
    success_url=reverse_lazy('home')

def myprofile(request):
    return render(request,'myprofile.html')

def appointment(request):
    form=customer_request.objects.all()
    return render(request,'appointment.html',{'form':form})

@login_required
def profile_update(request):
    form = update_profile(request.POST or None, instance=request.user)
    p_form = profile_pic_update(request.POST, request.FILES, instance=request.user.profile)
    if form.is_valid() and p_form.is_valid():
        form.save()
        p_form.save()
        return redirect('myprofile')
    context={'form':form,'p_form':p_form}
    return render(request,'profile_update.html', context)

def show(request, request_ID):
    show = customer_request.objects.get(pk=request_ID)
    return render(request,'show.html',{'show':show})

def delete_items(request, request_ID):
    item=customer_request.objects.get(pk=request_ID)
    item.delete()
    return redirect('appointment')

def delete_reviews(request, id):
    rev=review.objects.get(pk=id)
    rev.delete()
    return redirect('home')


def reviews(request):        
    if request.method == "POST":
        form=c_reviews(request.POST)
        if form.is_valid():
            update=form.save(commit=False)
            update.boss=request.user
            update.save()
    return redirect('/')

























# @login_required(login_url="/logins")
# def booking(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         phone=request.POST.get('phone')
#         address=request.POST.get('address')
#         city=request.POST.get('city')
#         state=request.POST.get('state')
#         pin=request.POST.get('pin')
#         req=request.POST.get('req')
#         desc=request.POST.get('desc')
#         dt=request.POST.get('dt')

#         book=customer_request(customer_name=name,email_ID=email,phone_number=phone,address=address,city=city,state=state,pin_code=pin,request_Type=req,description=desc,date=dt)
#         book.save()

#     books=customer_request.objects.all()
#     context={'bookings':books}
#     return render(request,'bookings.html', context)
from django.shortcuts import render, redirect,  get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def user_logIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('view_details')
        elif not username or not password:
            messages.warning(request, 'Please fill all fields.')
            return redirect('logIn')
        else:
            messages.warning(request, 'Email address and Password do not match, try again!')
            return redirect('/')
            
    return render(request, 'logIn.html')

def register(request):
     if request.method == 'POST':
        fName = request.POST.get('fullName')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeatPassword = request.POST.get('repeatPassword')
        if password == repeatPassword:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username is already taken')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Email is already taken')
            else:
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
                messages.success(request, 'Congratulatons! You successfully Registered')
                return redirect('logIn')
        else:
            messages.warning(request, 'Passwords do not match')   
     return render(request, 'register.html')
 
def add_details(request):
    # print('request =' , request)
    # print('request.user = ', request.user)
    if request.method == 'POST':
        payment_receiver = request.POST.get('payment_receiver')
        payment_amount = request.POST.get('payment_amount')
        payment_mode = request.POST.get('payment_mode')
        transaction_id = request.POST.get('transaction_id')
        payment_img = request.FILES.get('payment_img')
        if not all([payment_receiver, payment_amount, payment_mode, transaction_id, payment_img]):
        # if not payment_receiver or not payment_amount or not payment_mode or not transaction_id or not payment_img:
            messages.warning(request, 'Please fill in all fields, including the image.')
            return redirect('add_details')
        
        Detail.objects.create(
            user=request.user,
            payment_receiver = payment_receiver,
            payment_amount = payment_amount,
            mode_of_payment = payment_mode,
            transaction_id = transaction_id,
            Payment_img = payment_img,
        )
        messages.success(request, 'Your information has been added')
        return redirect('view_details')
    return render(request, 'add_details.html')

def user_logout(request):
    logout(request)
    return redirect('logIn')

def view_details(request):
    informations = Detail.objects.filter(user=request.user)
    context = {'details': informations}
    return render(request, 'view_details.html', context)

def delete_info(request, id):
    try:
        informations = Detail.objects.get(id=id)
    except Detail.DoesNotExist:
        return redirect('view_details')
    
    informations.delete()
    return redirect('view_details')

def edit_info(request, id):
    informations = get_object_or_404(Detail, id=id)
    if request.method == 'POST':
        payment_receiver = request.POST.get('payment_receiver')
        payment_amount = request.POST.get('payment_amount')
        payment_mode = request.POST.get('payment_mode')
        transaction_id = request.POST.get('transaction_id')
        payment_img = request.FILES.get('payment_img')
        
        informations.payment_receiver = payment_receiver
        informations.payment_amount = payment_amount
        informations.mode_of_payment = payment_mode
        informations.transaction_id = transaction_id
        if payment_img:
            informations.Payment_img = payment_img
        informations.save()  
        messages.success(request, 'Your information has been Updated')
        return redirect('view_details')
    
    context = {'detail': informations}
    return render(request, 'edit_details.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        Cfname = request.POST.get('Cfname')
        Cemail = request.POST.get('Cemail')
        Cphone = request.POST.get('Cphone')
        Cmassage = request.POST.get('Cmassage')
        
        if not Cfname or not Cemail or not Cphone or not Cmassage:
            # messages.warning(request, 'Please fill in all fields.')
            return redirect('contact')
        
        contact_instance = Contact(
            fname=Cfname,
            email=Cemail,
            phone=Cphone,
            massage=Cmassage
        )
        contact_instance.save()
        
    return render(request, 'contact.html')

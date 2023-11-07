from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecord
from .models import Record
from django.contrib.auth.models import User


# Login Function
def home(request):
    records = Record.objects.all()
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except Exception:
            messages.error(request, "User doesn't exits.")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username OR password doesn't exit.")
        
    context = {'records': records}
    return render(request, 'home.html', context=context)


# Logout Function
def logout_user(request):
    logout(request)
    messages.warning(request, "You have loggout successfully!")
    return redirect('home')



# Register Function
def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered!')
            return redirect('home')
        elif password1 !=password2:
            messages.warning(request, 'Your password and confirm password are not same!')
            return redirect('register')
        else:
            messages.warning(request, 'You have not enter correct date for registeration!')
            return redirect('register')
    else:
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'register.html', context=context)



# Customer Record

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        context = {'customer_record' : customer_record}
        return render(request, 'record.html', context=context)
    else:
        messages.warning(request, 'You must logged in to see the data!')
        return redirect('home')
    


# Delete Record
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, 'Record deleted successfully!')
        return redirect('home')
    else:
        messages.warning(request, 'You must logged in to delete record!')
        return redirect('home')
    


# Add Record
def add_record(request):
    user = request.user
    form = AddRecord()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddRecord(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Record added successfully...!')
                return redirect('home')
    else:
        messages.success(request, 'You must have to login to add record!')
        return redirect('home')
    context = {'form': form}
    return render(request, 'addrecord.html', context=context)
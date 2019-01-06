from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login
##### For Blog #########
from .models import blog

# Create your views here.
def index(request):
    #blog_n = blog.objects.all().order_by('date')
    return render(request,'signin_page/index.html',{})


def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request,user)
            return redirect('/')
    else:
        form = UserCreationForm()        

    context = {'form' : form}
    return render(request,'registration/register.html',context)



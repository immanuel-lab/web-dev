

from django.db.models.query_utils import RegisterLookupMixin
from django.shortcuts import redirect, render

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from app1.models import Destination,Form
from .views2 import RegisterForm
from django.contrib.auth.decorators import login_required

from .models import Editor
from .forms import Editor as ed

from django.contrib.auth import  authenticate,login
# Create your views here.




def navbar(request):
    return render(request,'navbar.html')



def home(request):
   # content={'name':'immanuel','book':'bible','published_date':'12.11.2019'}
   return render(request,'home.html')

def forms(request):
    return render(request,'forms.html')  

def form_submission(request):
  
        name=request.POST["txtUser"]
        email_id=request.POST["email"]
        gender=request.POST["rwdMale"]
        intrest=request.POST["intrest"]
        region=request.POST["region"]
        feedback=request.POST["feedback"]
        form=Form(name=name,email_id=email_id,gender=gender,intrest=intrest,region=region,feedback=feedback)
        form.save()
        return  redirect('home')
        
        
        

def visit(request):
   dest=Destination.objects.all()
   return render(request,'visit.html',{'dest':dest})





def register(request):
       # The request method 'POST' indicates
    # that the form was submitted
    if request.method == 'POST':  # 1
        # Create a form instance with the submitted data
        form = RegisterForm(request.POST)  # 2
        # Validate the form
        if form.is_valid(): 
            
            # If the form is valid, perform some kind of
            #username=form.cleaned_data.get('username')
            form.save()
            messages.success(request,'account created succesfully')
            # After the operation was successful,
            # redirect to some other page
            return redirect('home')  # 4
    else:  # 5
        # Create an empty form instance
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})




@login_required
def profile(request):
   return render(request,'profile.html')


def socialmedlog(request):
    return render(request,'socialmedlog.html')

@login_required
def editor(request):
    form=ed
    mydict={'form':form}
    

    
    return render(request,'editor.html',context=mydict)


def cked_save(request):
    
     title=request.POST["title"]
     body=request.POST["body"]
     form=Editor(title=title,body=body)
     form.save()
     return  redirect('news')
   
          
            
def salv(request):
    return render(request,'salvation.html')  




        
        
           
   

        
        

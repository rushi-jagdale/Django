
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Patient
# Create your views here.


# def home(request):
#     return render(request,'index.html')

# def login(request):

#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username = username, password = password)
#         if user is not None:
#             auth.login(request, user)   
#             return redirect('home')
#         else:
#             messages.info(request, 'invalid username and password')
#             return redirect('login')
#     else:
#         return render(request, 'login.html')

# def update(request):
#     all = Patient.objects.filter(name='Rishikesh')
#     return render(request,'/admin/includes/fieldset.html',{'data':all})

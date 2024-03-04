from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'signin.html', {"Success": "Login Success"}) 
        else:
            error_msg = form.errors.as_text()
            return render(request, 'login.html', {"Error": error_msg})

def register_view(request):
    return render(request, 'signup.html') 
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Message  
# Create your views here.
def index(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create and save the message instance
        Message.objects.create(first_name=first_name, last_name=last_name, email=email, message=message)

        return JsonResponse({'status': 'success', 'message': 'Your message has been sent successfully!'})
    return render(request,'index.html')



# views.py
from django.http import JsonResponse


from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
from django.core.paginator import Paginator
from . models import Song,Datas
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from django.core.mail import send_mail

def homes(request):
    dests = Datas.objects.all()
    print(dests)
    return render(request,'index.html',{'dests':dests})



def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Send email
        send_mail(
            subject,
            f"Email: {email}\n\n{message}",
            email,
            ['musafarshakeel@gmail.com'],  # Add recipient email address(es)
            fail_silently=False,
        )

        # Redirect or display success message
        return render(request, 'proj.html')

    return render(request, 'index.html')
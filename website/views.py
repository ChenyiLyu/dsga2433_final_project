from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def service(request):
    return render(request, 'service.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def contact(request):
    if request.method == 'POST':
        msg_name = request.POST['message-name']
        msg_email = request.POST['message-email']
        msg = request.POST['message']

        send_mail(
            'TEST: DSGA2433_Final_Project: ' + msg_name,
            msg,
            msg_email,
            ['lyuchenyi1997@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'contact.html', {'message_name': msg_name})
    return render(request, 'contact.html', {})

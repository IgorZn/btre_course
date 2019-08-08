from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.

def contact(request):
    if request.method == "POST":
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        contact = Contact(listing_id=listing_id, listing=listing, name=name, email=email, message=message,
                          user_id=user_id, phone=phone)

        contact.save()

        message.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('listing/'+listing_id)

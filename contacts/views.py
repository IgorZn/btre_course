from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
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

        # check if user already has made inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contact = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contact:
                messages.error(request, 'You have already made inquiry for this listing')
                return redirect('/listings/' + listing_id)

        contact = Contact(listing_id=listing_id, listing=listing, name=name, email=email, message=message,
                          user_id=user_id, phone=phone)

        contact.save()

        # Send email
        send_mail(
            'Subject here',
            'Here is the message. ' + listing,
            'igor.znamensky@gmail.com',
            [realtor_email, 'igor_znamenskii@epam.com'],
            fail_silently=False,
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)

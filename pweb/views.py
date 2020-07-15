from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Contact, Client, Image


def portfolio(request):
    return render( request, 'pweb/portfolio.html' )


def home(request):
    return render( request, 'pweb/base.html' )


def birth(request):
    return render( request, 'pweb/birth.html' )


def comment(request):
    return render( request, 'pweb/comment.html' )


def nav(request):
    return render( request, 'pweb/nav.html' )


def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get( 'email' )
        subject_r = request.POST.get( 'subject' )
        message_r = request.POST.get( 'message' )
        c = Contact( email=email_r, subject=subject_r, message=message_r )
        c.save()

        return render( request, 'pweb/thank.html' )
    else:
        return render( request, 'pweb/contact.html' )


def client(request):
    if request.method == 'POST':

        name = request.POST.get( 'name', '' )
        email = request.POST.get( 'email', '' )
        phone = request.POST.get( 'phone', '' )
        dob = request.POST.get( 'dob', '' )
        district = request.POST.get( 'district', '' )
        pro = request.POST.get( 'pro', '' )
        desc = request.POST.get( 'desc', '' )
        gender = request.POST.get( 'gender', '' )

        print( name, email, phone, district, pro, desc, dob, gender )
        if len( name ) > 10:
            messages.error( request, 'Enter valid name.Your name should be within 10 character', extra_tags='alert' )
            return redirect( 'birth_chart' )
        if not name.isalnum():
            messages.error( request, 'Enter Valid Name.Your name should be in letter and numbers', extra_tags='alert' )
            return redirect( 'birth_chart' )
        if len( phone ) > 10:
            messages.error( request, 'Enter valid Phone Numbers.Enter phone number within 10 digits.',
                            extra_tags='alert' )
            return redirect( 'birth_chart' )
        if len( desc ) > 100:
            messages.error( request, 'Enter queries within 100 words.',
                            extra_tags='alert' )
            return redirect( 'birth_chart' )

        cl = Client( gender=gender, name=name, desc=desc, phone=phone, email=email, dob=dob, district=district,
                     pro=pro )
        cl.save()
        return render( request, 'pweb/feedback.html' )


    else:
        return render( request, 'pweb/birth.html' )


def images(request):
    if request.method == 'POST':
        p = request.FILES[ 'picture1' ]
        p1 = request.FILES[ 'picture' ]
        name = request.POST.get( 'name_u', '' )
        email = request.POST.get( 'email_u', '' )
        phone = request.POST.get( 'phone_u', '' )
        dou = request.POST.get( 'dou', '' )
        desc = request.POST.get( 'desc1', '' )
        if len( name ) > 10:
            messages.error( request, 'Your name should be within 10 character', extra_tags='alert' )
            return redirect( 'birth_chart' )
        if not name.isalnum():
            messages.error( request, 'Your name should be in letter and numbers', extra_tags='alert' )
            return redirect( 'birth_chart' )
        if len( phone ) > 10:
            messages.error( request, 'Enter valid Phone Numbers.Enter phone number within 10 digits',
                            extra_tags='alert' )
            return redirect( 'birth_chart' )
        if len( desc ) > 100:
            messages.error( request, 'Enter queries within 100 words.',
                            extra_tags='alert' )

        im = Image( picture1=p, picture2=p1, name=name, email=email, phone=phone, desc1=desc, dou1=dou )
        im.save()
        return render( request, 'pweb/imagefeed.html' )

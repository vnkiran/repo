from django.shortcuts import render

from django.shortcuts import HttpResponse

from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.gis.geoip2 import GeoIP2

from .models import Contact


# Create your views here.

#https://www.svgbackgrounds.com/elements/animated-svg-preloaders/
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def family(request):
    return render(request, 'family.html')
def base(request):
    return render(request, 'base.html')
def child(request):
    return render(request, 'child.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')
        mobile = request.POST.get('mobile')
        location = request.POST.get('location')

        # Save the form data to the database
        contact = Contact.objects.create(
            name=name,
            email=email,
            description=description,
            mobile=mobile,
            location=location
        )

        # Show thank you message
        messages.success(request, 'Thank you for contacting us!')

        # Redirect to the same contact page after form submission
        return redirect('contact')

    return render(request, 'contact.html')
'''
        # Fetch the user's location based on IP address
        try:
            g = GeoIP2()
            user_ip = request.META.get('REMOTE_ADDR')
            location = g.city(user_ip)
            contact.location = f"{location.get('city', '')}, {location.get('country_name', '')}"
            contact.save()
        except Exception as e:
            # In case of any error, location will remain blank
            pass

        messages.success(request, 'Thank you for contacting us!')
        return redirect('contact')

    return render(request, 'contact.html')

'''

'''
def upload(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES['image']
        video = request.FILES['video']
        text = request.POST.get('text')
        data =Upload.objects.create(title=title, image=image, video=video, text=text)
        
        return render(request, 'success.html')
    return render(request, 'upload.html')

'''
from django.core.exceptions import ValidationError

def upload(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        video = request.FILES.get('video')
        text = request.POST.get('text')

        if video:
            # Process the video file if uploaded
            pass
        else:
            video = None


        data = User.objects.create(name=name, image=image, video=video, text=text)
        data.save()
                
        return render(request, 'success.html')
               
    return render(request, 'upload.html')

def retrieve(request):
    uploads = User.objects.all().order_by('-posted_at')
    return render(request, 'retrieve.html', {'uploads': uploads})

        
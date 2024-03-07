from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Hero, AboutUs, Testimonials, Features, OurTeam, FAQ, Contact_Forms, Contact_Info
# Create your views here.
def home(request):
    context = {
        'hero': Hero.objects.all(),
        'about_us': AboutUs.objects.all(),
        'testimonials': Testimonials.objects.all(),
        'our_team': OurTeam.objects.all(),
        'faqs': FAQ.objects.all(),
        'features' : Features.objects.all(),
        'contact_info': Contact_Info.objects.all(),
    }
    return render(request, 'homepage/index.html', context)

def contact (request):

    context = {
        'contact_info': Contact_Info.objects.all(),
    }

    if request.method == 'POST':
        contact = Contact_Forms()
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.subject = request.POST['subject']
        contact.message = request.POST['message']
        contact.save()

        messages.success(request,'Thank You')  # Add success message

            # # Send email using Django's email function
        # send_mail(
        #     'RoughCutSolutions Contact Form Submission',
        #     f'Subject: {contact.subject}\nName: {contact.name}\nEmail: {contact.email}\nMessage: {contact.message}',
        #     contact.email,
        #     ['larsenj2064@gmail.com'],
        #     fail_silently=False,
        # )
        return HttpResponseRedirect("/")
    else:
        return render(request, 'homepage/elements/contact_page.html', context)  
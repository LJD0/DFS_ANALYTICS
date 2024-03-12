from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Hero, AboutUs, Testimonials, Features, OurTeam, FAQ, Contact_Forms, Contact_Info, expo_info
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

        messages.success(request,'Thank You', extra_tags='contact',)  # Add success message

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

def new_review (request):

    context = {
    }

    if request.method == 'POST':
        testimonial = Testimonials()
        testimonial.full_name = request.POST['name']
        testimonial.job_title = request.POST['job_title']
        testimonial.stars = request.POST['stars']
        testimonial.topic = request.POST['topic']
        testimonial.review = request.POST['message']
        testimonial.save()

        messages.success(request,'Thank You', extra_tags='testimonial',)  # Add success message

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
        return render(request, 'homepage/elements/testimonials_page.html', context)


def dfs_welcome (request):
    context = {
        expo_info: expo_info.objects.all(),
    }
    return render(request, 'expo/expo_page.html', context)


def new_review (request):

    context = {
    }

    if request.method == 'POST':
        testimonial = Testimonials()
        testimonial.full_name = request.POST['name']
        testimonial.job_title = request.POST['job_title']
        testimonial.stars = request.POST['stars']
        testimonial.topic = request.POST['company']
        testimonial.review = request.POST['message']
        testimonial.save()

        messages.success(request,'Thank You', extra_tags='testimonial',)  # Add success message


        #export response and add to csv
        import csv
        from datetime import datetime 
        from django.http import HttpResponse
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="testimonials.csv"'
        writer = csv.writer(response)
        writer.writerow(['Full Name', 'Job Title', 'Stars', 'Topic', 'Review', 'Date'])
        writer.writerow([testimonial.full_name, testimonial.job_title, testimonial.stars, testimonial.topic, testimonial.review, datetime.now()])
    

    
        
        
        
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
        return render(request, 'homepage/elements/testimonials_page.html', context)
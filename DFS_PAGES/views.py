from django.shortcuts import render
from django.apps import apps
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from .models import Hero, AboutUs, Testimonials, OurTeam, FAQ, Contact_Forms, Contact_Info, expo_info, expo_form, HomePage, Services, Tabs, Solutions, solutions_item
import csv
# Create your views here.
def home(request):
    context = {
        'hero': Hero.objects.all(),
        'about_us': AboutUs.objects.all(),
        'services': Services.objects.all(),
        'tabs': Tabs.objects.all(),
        'solutions': Solutions.objects.all(),
        'solutions_item': solutions_item.objects.all(),
        'testimonials': Testimonials.objects.all(),
        'our_team': OurTeam.objects.all(),
        'faqs': FAQ.objects.all(),
        'contact_info': Contact_Info.objects.all(),
        'homepage': HomePage.objects.first(),
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



def dfs_welcome (request):
    context = {
        'expo_info': expo_info.objects.all(),
    }
 
    return render(request, 'expo/expo_page.html', context)

def dfs_expo (request):
    context = {
        expo_info: expo_info.objects.all(),
    }

    if request.method == 'POST':
        exponw = expo_form()
        exponw.full_name = request.POST['name']
        exponw.email = request.POST['email']
        exponw.company = request.POST['company']
        exponw.phone = request.POST['phone']
        exponw.package = request.POST['package']
        exponw.save()
        return HttpResponseRedirect("/expothanks")

        messages.success(request,'Thank You', extra_tags='contact',)
    return render(request, 'expo/expo_form_page.html', context)

def thankspage (request):
    return render(request, 'expo/expothanks.html')

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

def download_model_csv(request, model):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}_data.csv"'.format(model.__name__)

    writer = csv.writer(response)
    
    # Get column names from the model
    model_fields = [field.name for field in model._meta.fields]
    writer.writerow(model_fields)

    # Get data from the model
    queryset = model.objects.all()
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in model_fields])

    return response

def redirect_to_download(request):
    model_name = request.GET.get('model')
    if model_name:
        model = apps.get_model(app_label='DFS_PAGES', model_name=model_name)
        if model:
            return download_model_csv(request, model)
    return redirect(reverse('expothanks'))
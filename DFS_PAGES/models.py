from django.db import models

# Create your models here.

class Hero(models.Model):
    name = "Hero"
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='')
    button = models.TextField()

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    name = "About Us"
    tag = models.CharField(default=None, max_length=100)
    title = models.CharField(max_length=100)
    about = models.TextField(blank=True)
    image = models.ImageField(upload_to='')
    button = models.CharField(default=None,max_length=50)

    def __str__(self):
        return self.name

class Testimonials(models.Model):
    RATINGS = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    stars = models.IntegerField(default=5,choices=RATINGS)
    company = models.CharField(max_length=100, blank=True)
    review = models.TextField()
    # image = models.ImageField(upload_to='testimonials/', blank=True)
    on_homepage = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name


class OurTeam(models.Model):
    name = "Our Team"
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    linkedin_link = models.CharField(max_length=200, blank=True)
    blurb = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.question

class Contact_Forms(models.Model):
    name = models.CharField(max_length=100,blank=True)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Contact_Info(models.Model):
    name = "DFS Analytics"
    # address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class expo_info(models.Model):
    name = "Expo Info"
    page_title = models.CharField(max_length=100)
    page_subtitle = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    button = models.CharField(max_length=100)
    video_link = models.CharField(max_length=200)
    video_title = models.CharField(max_length=100)
    video_subtitle = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class expo_form(models.Model):
    name = "Expo Form"
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    how_heard = models.CharField(max_length=100,default='Expo West')    
    package = models.CharField(max_length=100,choices=[('D/M Report','Demo/Merchandising Report'),('PEA','Promotion Efficacy Analysis'),])

    def __str__(self):
        return self.full_name


class HomePage(models.Model):
    name = "Home Page"
    hero = models.BooleanField(default=True)
    about_us = models.BooleanField(default=True)
    services = models.BooleanField(default=True)
    tabs = models.BooleanField(default=True)
    solutions = models.BooleanField(default=True)
    testimonials = models.BooleanField(default=True)
    our_team = models.BooleanField(default=False)
    faqs = models.BooleanField(default=False)
    contact = models.BooleanField(default=True)
    


    def __str__(self):
        return self.name


class Services(models.Model):
    name = "Services Section"
    services_tag = models.CharField(max_length=100)
    services_title = models.CharField(max_length=100)
    services_1 = models.CharField(max_length=500)
    services_2 = models.CharField(max_length=500)
    services_3 = models.CharField(max_length=500)
    services_4 = models.CharField(max_length=500)
    services_5 = models.CharField(max_length=500)
    services_6 = models.CharField(max_length=500)
    services_image = models.ImageField(upload_to='')

    def __str__(self):
        return self.name

class Tabs(models.Model):
    name = "Tabs Section"
    tabs_title = models.CharField(max_length=100)
    tabs_image = models.ImageField(upload_to='')

    tabs_tab1 = models.CharField(default=None, max_length=100)
    tabs_tab1_text = models.CharField(max_length=500)
    tabs_tab1_bullet1 = models.CharField(max_length=100)
    tabs_tab1_bullet_blurb1 = models.CharField(max_length=500)
    tabs_tab1_bullet2 = models.CharField(max_length=100)
    tabs_tab1_bullet_blurb2 = models.CharField(max_length=500)
    tabs_tab1_bullet3 = models.CharField(max_length=100, blank=True)
    tabs_tab1_bullet_blurb3 = models.CharField(max_length=500, blank=True)

    tabs_tab2 = models.CharField(default=None, max_length=100)
    tabs_tab2_text = models.CharField(max_length=500)
    tabs_tab2_bullet1 = models.CharField(max_length=100)
    tabs_tab2_bullet_blurb1 = models.CharField(max_length=500)
    tabs_tab2_bullet2 = models.CharField(max_length=100)
    tabs_tab2_bullet_blurb2 = models.CharField(max_length=500)
    tabs_tab2_bullet3 = models.CharField(max_length=100, blank=True)
    tabs_tab2_bullet_blurb3 = models.CharField(max_length=500, blank=True)

    tab3 = models.BooleanField(default=False)
    tabs_tab3 = models.CharField(default=None, max_length=100)
    tabs_tab3_text = models.CharField(max_length=500)
    tabs_tab3_bullet1 = models.CharField(max_length=100)
    tabs_tab3_bullet_blurb1 = models.CharField(max_length=500)
    tabs_tab3_bullet2 = models.CharField(max_length=100)
    tabs_tab3_bullet_blurb2 = models.CharField(max_length=500)
    tabs_tab3_bullet3 = models.CharField(max_length=100, blank=True)
    tabs_tab3_bullet_blurb3 = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class solutions_item(models.Model):
    name = "Solutions item"
    solutions_item = models.CharField(max_length=100)
    solutions_item_blurb = models.CharField(max_length=500)
    solutions_item_icon = models.CharField(max_length=100)
    def __str__(self):
        return self.solutions_item

class Solutions(models.Model):
    name = "Solutions Section"
    solutions_title = models.CharField(max_length=100)
    solutions_image = models.ImageField(upload_to='')

    solutions_items = models.ManyToManyField('solutions_item', related_name='solutions', blank=True)

    def __str__(self):
        return self.name
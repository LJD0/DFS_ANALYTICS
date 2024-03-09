from django.db import models

# Create your models here.
class Pages(models.Model):
    content = models.TextField()
    button_text = models.CharField(max_length=100)
    last_update = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)
    section= models.CharField(max_length=100)

    def __str__(self):
        return self.section


class title_line(models.Model):
    placement = models.ForeignKey(Pages, related_name='title_lines', on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

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
    topic = models.CharField(max_length=100, blank=True)
    review = models.TextField()
    # image = models.ImageField(upload_to='testimonials/', blank=True)
    on_homepage = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name

class Features(models.Model):
    name = "Features"
    services_tag = models.CharField(max_length=100)
    services_title = models.CharField(max_length=100)
    services_1 = models.CharField(max_length=500)
    services_2 = models.CharField(max_length=500)
    services_3 = models.CharField(max_length=500)
    services_4 = models.CharField(max_length=500)
    services_5 = models.CharField(max_length=500)
    services_6 = models.CharField(max_length=500)
    services_image = models.ImageField(upload_to='')

    growth_title = models.CharField(max_length=100)
    growth_image = models.ImageField(upload_to='')

    growth_tab1_name = models.CharField(default=None, max_length=100)
    growth_tab1_blurb1 = models.CharField(max_length=500)
    growth_tab1_title1 = models.CharField(max_length=100)
    growth_tab1_blurb2 = models.CharField(max_length=500)
    growth_tab1_title2 = models.CharField(max_length=100)
    growth_tab1_blurb3 = models.CharField(max_length=500)
    growth_tab1_title3 = models.CharField(max_length=100, blank=True)
    growth_tab1_blurb4 = models.CharField(max_length=500, blank=True)

    growth_tab2_name = models.CharField(max_length=100)
    growth_tab2_blurb1 = models.CharField(max_length=500)
    growth_tab2_title1 = models.CharField(max_length=100)
    growth_tab2_blurb2 = models.CharField(max_length=500)
    growth_tab2_title2 = models.CharField(max_length=100)
    growth_tab2_blurb3 = models.CharField(max_length=500)
    growth_tab2_title3 = models.CharField(max_length=100, blank=True)
    growth_tab2_blurb4 = models.CharField(max_length=500, blank=True)

    growth_tab3_name = models.CharField(max_length=100)
    growth_tab3_blurb1 = models.CharField(max_length=500)
    growth_tab3_title1 = models.CharField(max_length=100)
    growth_tab3_blurb2 = models.CharField(max_length=500)
    growth_tab3_title2 = models.CharField(max_length=100)
    growth_tab3_blurb3 = models.CharField(max_length=500)
     

    tools_title = models.CharField(max_length=100)
    tools_image = models.ImageField(upload_to='')

    tools_item1 = models.CharField(max_length=100)
    tools_item1_blurb = models.CharField(max_length=500)
    tools_item2 = models.CharField(max_length=100)
    tools_item2_blurb = models.CharField(max_length=500)
    tools_item3 = models.CharField(max_length=100)
    tools_item3_blurb = models.CharField(max_length=500)
    tools_item4 = models.CharField(max_length=100)
    tools_item4_blurb = models.CharField(max_length=500)
    tools_item5 = models.CharField(max_length=100)
    tools_item5_blurb = models.CharField(max_length=500)
    tools_item6 = models.CharField(max_length=100)
    tools_item6_blurb = models.CharField(max_length=500)


    def __str__(self):
        return self.name

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
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Contact_Info(models.Model):
    name = "DFS Analytics"
    # address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.name
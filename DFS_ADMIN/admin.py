from django.contrib import admin
from django.contrib.admin import AdminSite

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from DFS_PAGES.models import Hero, AboutUs, Testimonials, Features, OurTeam, FAQ, Contact_Forms, Contact_Info, expo_info
# Register your models here.

class DFS_AdminSite(AdminSite):
    site_header = 'DFS Admin'
    site_title = 'DFS Admin Portal'
    index_title = 'Welcome to DFS Admin Portal'

class Contact_FormsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'message', 'created_at')
    list_filter = ('full_name', 'email', 'subject', 'message', 'created_at')
    search_fields = ('full_name', 'email', 'subject', 'message', 'created_at')
    ordering = ['created_at']
    list_per_page = 10

class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title', 'review', 'stars', 'on_homepage', 'created_at')
    list_filter = ('full_name', 'job_title', 'review', 'stars', 'on_homepage', 'created_at')
    search_fields = ('full_name', 'job_title', 'review', 'stars', 'on_homepage', 'created_at')
    ordering = ['created_at']
    list_per_page = 10

dfs_admin = DFS_AdminSite(name='admin')
dfs_admin.register(User, UserAdmin)
dfs_admin.register(Hero)
dfs_admin.register(AboutUs)
dfs_admin.register(Testimonials, TestimonialsAdmin)
dfs_admin.register(Features)
dfs_admin.register(OurTeam)
dfs_admin.register(FAQ)
dfs_admin.register(Contact_Forms, Contact_FormsAdmin)
dfs_admin.register(Contact_Info)
dfs_admin.register(expo_info)



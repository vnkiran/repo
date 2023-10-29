from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Contact)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name','image','video','text','posted_at')
    list_display_links = ('name','image','video')
    list_filter = ('posted_at')
    list_editable = ('name', 'text', 'image', 'video')

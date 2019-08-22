from django.contrib import admin
from .models import Profil

# Register your models here.

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('user',)

    list_filter = ('user',)
    search_fields = ['user']
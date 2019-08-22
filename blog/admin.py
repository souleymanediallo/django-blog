from django.contrib import admin
from .models import Category, Post
from .forms import CategoryAdminForm, PostAdminForm

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm

    list_display = ('name', 'created_date', 'updated_date',)
    list_display_links = ('name',)
    search_fields = ['name']
    exclude = ('created_date', 'updated_date')

    prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

    list_display = ('title', 'created_date', 'updated_date',)
    list_display_links = ('title',)
    search_fields = ['title']
    exclude = ('created_date', 'updated_date')

    prepopulated_fields = {'slug': ('title',)}


from django import forms
from .models import Category, Post

class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('created_date', 'updated_date')

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('created_date', 'updated_date')
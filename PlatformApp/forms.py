from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Review


class ProjectReviewForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, label='')
    class Meta:
        model = Review
        fields = ["content"]

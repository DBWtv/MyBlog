import re
from django import forms
from django.core.exceptions import ValidationError
from .models import UserProfile


class RegUserProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['about_yourself', 'phone_number']
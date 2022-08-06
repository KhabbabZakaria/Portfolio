from email.policy import default
from time import timezone
from django import forms
import datetime
from .models import Post


class FeedbackForm(forms.ModelForm):
    author = forms.CharField(label='Your name without spaces', max_length=100)
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Your feedback',widget=forms.Textarea())
    datePosted = forms.DateField(label='Date of posting',initial=datetime.date.today)

    class Meta:
        model = Post
        fields = ('author', 'title', 'description', 'datePosted')
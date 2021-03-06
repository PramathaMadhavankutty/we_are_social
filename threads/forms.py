from django import forms
from .models import Thread, Posts


class ThreadForm(forms.ModelForm):

    name = forms.CharField(label='Thread name')
    is_a_poll = forms.BooleanField(label='Include a poll?', required=False)

    class Meta:
        model = Thread
        fields = ['name']


class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ['comment']

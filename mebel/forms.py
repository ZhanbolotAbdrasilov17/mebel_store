from django import forms

from .models import Email


class MailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('address',)
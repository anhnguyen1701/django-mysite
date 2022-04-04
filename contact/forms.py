from django import forms

from contact.models import contactForm


class contact_Form(forms.ModelForm):
    class Meta:
        model = contactForm
        fields = ['username', 'email', 'body']

from django import forms
from .models import Feedback
from .models import contact

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedbackfields = ['comment']
        widegts = {
            'comment': forms.Textarea(attrs={'rows':,
            'placeholder': 'enter your feedback here...'
            }),
        }

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['name', 'email']        
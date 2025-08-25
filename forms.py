from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedbackfields = ['comment']
        widegts = {
            'comment': forms.Textarea(attrs={'rows':,
            'placeholder': 'enter your feedback here...'
            }),
        }
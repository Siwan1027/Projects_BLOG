from django import forms
from .models import Posting
class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        exclude = ('created_at', 'updated_at')
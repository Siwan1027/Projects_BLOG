# board/forms.py
from django import forms
from .models import Posting, Reply

class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        exclude = ('created_at', 'updated_at')
    
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('content',)
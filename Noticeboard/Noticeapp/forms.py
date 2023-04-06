from django import forms
from .models import Notice
 
 
class Noticeform(forms.ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'


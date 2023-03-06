from django import forms
from .models import UserProfile, Comment

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('receive_promotions',)
        labels = {
            'receive_promotions': 'Receber promoções'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        labels = {
            'comment': 'Comentário',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 6, 'cols': 15})
        }
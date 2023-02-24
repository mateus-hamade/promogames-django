from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('receive_promotions',)
        labels = {
            'receive_promotions': 'Receber promoções'
        }
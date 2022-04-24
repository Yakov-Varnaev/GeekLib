from django import forms

from .models import BookRent


class RentForm(forms.ModelForm):
    class Meta:
        model = BookRent
        fields = ('to_date',)
        widgets = {
            'to_date': forms.DateInput(attrs={'type':'date'})
        }
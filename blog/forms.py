from django import forms
from .models import Custom_User

class CustomForm(forms.ModelForm):
    class Meta:
        model = Custom_User
        fields = [
            'first_name',
            'last_name',
            'fathers_name',
            'gender',
            'email_id',
            'phone_number',
            'spouse_name'
        ]

from .models import Profile, User
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

# Create your forms here.
class ChangePasswordForm( PasswordChangeForm ):
    class Meta:
        model = Profile
        fields = (
            'old_password',
            'new_password1',
            'new_password2',
        )

    def __init__(self, *args, **kwargs):
        super( ChangePasswordForm, self ).__init__( *args, **kwargs )

        self.fields['old_password'].widget = forms.PasswordInput( attrs={'class': 'form-control', 'type': 'password'} )
        self.fields['new_password1'].widget = forms.PasswordInput( attrs={'class': 'form-control', 'type': 'password'} )
        self.fields['new_password2'].widget = forms.PasswordInput( attrs={'class': 'form-control', 'type': 'password'} )
        
class UpdateProfilePageForm( forms.ModelForm ):
    class Meta:
        model = Profile
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'bio',
            'avatar',
        )
        
class UpdateUserPageForm( forms.ModelForm ):
    email = forms.EmailField()
    username = forms.TextInput()

    class Meta:
        model = User
        fields = (
            'email',
            'username',
        )
        
    widgets = {
            'email': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'id_email', 'type': 'email'}),
        }

        
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     qs = User.objects.filter(email=email)
    #     if qs.exists():
    #         raise forms.ValidationError("Email is already taken.")
    #     return email
    
    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     qs = User.objects.filter(username=username)
    #     if qs.exists():
    #         raise forms.ValidationError("Username is already taken.")
    #     return username
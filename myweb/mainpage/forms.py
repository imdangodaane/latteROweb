from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password, check_password
from .models import Login
from django.contrib.auth.models import User
from datetime import datetime

class SignupForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput,
                                       help_text="Re-enter your password.")

    class Meta:
        model = Login
        fields = ('userid', 'user_pass', 'password_confirm', 'sex', 'email',)

        labels = {
            'username': _('Username'),
            'email': _('Email address *'),
            'user_pass': _('Password'),
            'password_confirm': _('Password confirmation'),
        }
        widgets = {
            'password': forms.PasswordInput,
            'password_confirm': forms.PasswordInput,
            'email_address': forms.EmailInput,
        }
        help_texts = {
            # 'username': _('Username may only contain alphanumeric characters\
            #               or single hyphens,and cannot begin or end with a hy\
            #               phen.'),
            # 'password': _("Make sure it's more than 15 characters OR at least\
            #               8 characters including a number and a lowercase let\
            #               ter."),
            # 'password_confirm': _("Re-enter your password.",)
        }
        error_messages = {
            'username': {
                'max_length': _("This username is too long."),
            },
        }

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get('user_pass')
        password_confirm = cleaned_data.get('password_confirm')
        if not check_password(password_confirm, password):
            raise forms.ValidationError(
                'Password and confirmation password does not match.'
            )
        username_list = list(Login.objects.values_list('userid', flat=True))
        username = cleaned_data.get('userid')
        if username in username_list:
            raise forms.ValidationError(
                'This name has exist, please choose another name.'
            )

    def clean_password(self):
        encrypt_password = make_password(self.cleaned_data['user_pass'])
        if encrypt_password:
            return encrypt_password
        else:
            raise forms.ValidationError(
                'Password encryption fail, please choose another password'
            )

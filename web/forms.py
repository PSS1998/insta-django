from django import forms

from .models import Account, AccountSetting

class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('username', 'password',)

class AccountSettingForm(forms.ModelForm):

    class Meta:
        model = AccountSetting
        fields = ('tag',)

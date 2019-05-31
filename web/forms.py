from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Account, AccountSetting

class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('username', 'password',)

class AccountSettingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AccountSettingForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        # self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'form-inline'
        # self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-lg-2 col-md-2'
        # self.helper.field_class = 'col-lg-8 col-md-8'
        self.helper.form_method = 'post'
        # self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Submit'))

        self.fields['tag_list'].help_text = "seperate each tag with comma(,)"
        self.fields['tag_blacklist'].help_text = "seperate each tag with comma(,)"
        self.fields['user_blacklist'].help_text = "seperate each tag with comma(,)"
        self.fields['comment_list'].help_text = "seperate each tag with comma(,)"
        self.fields['unwanted_username_list'].help_text = "seperate each tag with comma(,)"
        self.fields['unfollow_whitelist'].help_text = "seperate each tag with comma(,)"
        self.fields['tag_list'].required = False
        self.fields['tag_blacklist'].required = False
        self.fields['user_blacklist'].required = False
        self.fields['comment_list'].required = False
        self.fields['unwanted_username_list'].required = False
        self.fields['unfollow_whitelist'].required = False
    # tag_list = forms.ModelChoseField(label='Tag List', help_text='seperate each tag with comma(,)')

    class Meta:
        model = AccountSetting
        fields = ('active', 'like', 'comment', 'like_per_day', 'comments_per_day', 'tag_list', 'tag_blacklist', 'user_blacklist', 'max_like_for_one_tag', 'follow_per_day', 'follow_time', 'unfollow_per_day', 'comment_list', 'unwanted_username_list', 'unfollow_whitelist',)

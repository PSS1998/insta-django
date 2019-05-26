from django.contrib import admin
from .models import Account, Token, AccountSetting

# Register your models here.

admin.site.register(Account)
admin.site.register(Token)
admin.site.register(AccountSetting)

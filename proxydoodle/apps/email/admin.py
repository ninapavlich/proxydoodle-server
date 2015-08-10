from django.contrib import admin

from carbon.compounds.email.admin import EmailTemplateAdmin as BaseEmailTemplateAdmin
from carbon.compounds.email.admin import EmailCategoryAdmin as BaseEmailCategoryAdmin
from carbon.compounds.email.admin import EmailReceiptAdmin as BaseEmailReceiptAdmin
from carbon.compounds.email.admin import EmailCategorySubscriptionSettingsAdmin as BaseEmailCategorySubscriptionSettingsAdmin
from carbon.compounds.email.admin import EmailCategorySubscriptionSettingsInline as BaseEmailCategorySubscriptionSettingsInline
from carbon.compounds.email.admin import UserSubscriptionSettingsAdmin as BaseUserSubscriptionSettingsAdmin


from .models import *


class EmailTemplateAdmin(BaseEmailTemplateAdmin):
    
    pass


class EmailCategoryAdmin(BaseEmailCategoryAdmin):

    pass


class EmailReceiptAdmin(BaseEmailReceiptAdmin):

    pass


class EmailCategorySubscriptionSettingsAdmin(BaseEmailCategorySubscriptionSettingsAdmin):
    pass

class EmailCategorySubscriptionSettingsInline(BaseEmailCategorySubscriptionSettingsInline):
    model = EmailCategorySubscriptionSettings  

class UserSubscriptionSettingsAdmin(BaseUserSubscriptionSettingsAdmin):
    inlines = [EmailCategorySubscriptionSettingsInline]


admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(EmailCategory, EmailCategoryAdmin)
admin.site.register(EmailReceipt, EmailReceiptAdmin)
admin.site.register(EmailCategorySubscriptionSettings, EmailCategorySubscriptionSettingsAdmin)
admin.site.register(UserSubscriptionSettings, UserSubscriptionSettingsAdmin)
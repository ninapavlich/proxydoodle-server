from django.contrib import admin

from carbon.compounds.account.admin import UserAdmin as BaseUserAdmin
from carbon.compounds.account.admin import OrganizationAdmin as BaseOrganizationAdmin
from carbon.compounds.account.admin import UserGroupMemberInGroupAdmin as BaseUserGroupMemberInGroupAdmin
from carbon.compounds.account.admin import UserGroupMemberInUserAdmin as BaseUserGroupMemberInUserAdmin
from carbon.compounds.account.admin import UserGroupAdmin as BaseUserGroupAdmin
from carbon.compounds.account.admin import SocialContactLinkInline as BaseSocialContactLinkInline

from .models import *


class UserGroupMemberInGroupAdmin(BaseUserGroupMemberInGroupAdmin):
    model = UserGroupMember    

class UserGroupMemberInUserAdmin(BaseUserGroupMemberInUserAdmin):
    model = UserGroupMember    

class SocialContactLinkInline(BaseSocialContactLinkInline):
    model = SocialContactLink    

class UserAdmin(BaseUserAdmin):
    inlines = [UserGroupMemberInUserAdmin, SocialContactLinkInline]

class UserGroupAdmin(BaseUserGroupAdmin):
    inlines = [UserGroupMemberInGroupAdmin]

class OrganizationAdmin(BaseOrganizationAdmin):
    pass
    

admin.site.register(Organization, OrganizationAdmin)    
admin.site.register(User, UserAdmin)
admin.site.register(UserGroup, UserGroupAdmin)
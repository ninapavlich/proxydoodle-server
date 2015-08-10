from django.db import models
from django.conf import settings

from carbon.compounds.account.models import User as BaseUser
from carbon.compounds.account.models import Address as BaseAddress
from carbon.compounds.account.models import UserGroup as BaseUserGroup
from carbon.compounds.account.models import UserGroupMember as BaseUserGroupMember
from carbon.compounds.account.models import Organization as BaseOrganization
from carbon.compounds.account.models import OrganizationMember as BaseOrganizationMember
from carbon.compounds.account.models import SocialContactLink as BaseSocialContactLink


class User(BaseUser):

	pass

class Address(BaseAddress):

	pass

class UserGroupMember(BaseUserGroupMember):

	group = models.ForeignKey('account.UserGroup', 
		blank=True, null=True)    

class UserGroup(BaseUserGroup):
	member_class = UserGroupMember
	pass    


class Organization(BaseOrganization):

	pass

class OrganizationMember(BaseOrganizationMember):

	organization = models.ForeignKey('Organization', blank=True, null=True)

class SocialContactLink(BaseSocialContactLink):
	pass
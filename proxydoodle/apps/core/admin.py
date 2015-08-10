from django.contrib import admin

from carbon.compounds.core.admin import TemplateAdmin as BaseTemplateAdmin
from carbon.compounds.core.admin import CSSPackageAdmin as BaseCSSPackageAdmin
from carbon.compounds.core.admin import JSPackageAdmin as BaseJSPackageAdmin

from carbon.compounds.core.admin import CSSResourceAdmin as BaseCSSResourceAdmin
from carbon.compounds.core.admin import JSResourceAdmin as BaseJSResourceAdmin
from carbon.compounds.core.admin import CSSResourceInline as BaseCSSResourceInline
from carbon.compounds.core.admin import JSResourceInline as BaseJSResourceInline

from carbon.compounds.core.admin import MenuItemInline as BaseMenuItemInline
from carbon.compounds.core.admin import MenuItemAdmin as BaseMenuItemAdmin
from carbon.compounds.core.admin import AdminAppLinkInline as BaseAdminAppLinkInline
from carbon.compounds.core.admin import AdminLinkInline as BaseAdminLinkInline
from carbon.compounds.core.admin import AdminAppGroupAdmin as BaseAdminAppGroupAdmin
from carbon.compounds.core.admin import AdminSidebarAdmin as BaseAdminSidebarAdmin

from carbon.compounds.core.admin import LegacyURLRefererInline as BaseLegacyURLRefererInline
from carbon.compounds.core.admin import LegacyURLAdmin as BaseLegacyURLAdmin

from .models import *

class TemplateAdmin(BaseTemplateAdmin):
    pass


class CSSResourceAdmin(BaseCSSResourceAdmin):
    pass

class JSResourceAdmin(BaseJSResourceAdmin):
    pass

class CSSResourceInline(BaseCSSResourceInline):
    model = CSSResource

class JSResourceInline(BaseJSResourceInline):
    model = JSResource

class CSSPackageAdmin(BaseCSSPackageAdmin):
    inlines = [CSSResourceInline]

class JSPackageAdmin(BaseJSPackageAdmin):
    inlines =[JSResourceInline]    


class MenuItemInline(BaseMenuItemInline):
    model = MenuItem
    
class MenuItemAdmin(BaseMenuItemAdmin):
    inlines = [MenuItemInline]


class AdminAppLinkInline(BaseAdminAppLinkInline):
    model = AdminAppLink

class AdminLinkInline(BaseAdminLinkInline):

    model = AdminLink
  
class AdminAppGroupAdmin(BaseAdminAppGroupAdmin):
    inlines = [AdminAppLinkInline]

class AdminSidebarAdmin(BaseAdminSidebarAdmin):
    inlines = [AdminLinkInline]


class LegacyURLRefererInline(BaseLegacyURLRefererInline):
    model = LegacyURLReferer
    
class LegacyURLAdmin(BaseLegacyURLAdmin):
    inlines = [LegacyURLRefererInline]    
    pass




admin.site.register(Template, TemplateAdmin)
admin.site.register(CSSPackage, CSSPackageAdmin)
admin.site.register(JSPackage, JSPackageAdmin)
admin.site.register(CSSResource, CSSResourceAdmin)
admin.site.register(JSResource, JSResourceAdmin)

admin.site.register(AdminAppGroup, AdminAppGroupAdmin)
admin.site.register(AdminSidebar, AdminSidebarAdmin)
admin.site.register(LegacyURL, LegacyURLAdmin)
admin.site.register(MenuItem, MenuItemAdmin)

from django.contrib import admin
from django.core.urlresolvers import reverse

from carbon.compounds.page.admin import PageAdmin as BasePageAdmin
from carbon.compounds.page.admin import PageTagAdmin as BasePageTagAdmin
from carbon.compounds.page.admin import PageContentBlockInline as BasePageContentBlockInline


from django_inline_wrestler.admin import TabularInlineOrderable

from .models import *

class PageSlideAdmin(TabularInlineOrderable):
    
    model = PageSlide
    extra = 0

    autocomplete_lookup_fields = {
        'fk': ('slide_image',),
    }
    raw_id_fields = ( 'slide_image',)

    def preview(self, obj):
        if obj.slide_image:
            try:
                return "<img src='%s' alt='%s preview'/>"%(obj.slide_image.thumbnail.url, obj.slide_image.title)
            except:
                return ""
        return ''
    preview.allow_tags = True

    def edit_image(self, obj):
        style="style='width:278px;display:block;'"
        if obj.slide_image.pk:
            
            try:
                object_type = type(obj.slide_image).__name__
                url = reverse('admin:%s_%s_change' %(obj.slide_image._meta.app_label,  obj.slide_image._meta.model_name),  args=[obj.slide_image.id] )
                return '<a href="%s" %s>Edit Image &gt;</a>'%(url, style)
            except:
                return '<span %s>&nbsp;</span>'%(style)
        return '<span %s>&nbsp;</span>'%(style)
    edit_image.allow_tags = True


    readonly_fields = ('preview','edit_image')
    fields = (
        'order',
        'slide_image',
        'preview',
        'edit_image',
        'link'
    )

class PageContentBlockInline(BasePageContentBlockInline):
    model = PageContentBlock   

class PageAdmin(BasePageAdmin):
    inlines = [PageSlideAdmin, PageContentBlockInline]



class PageTagAdmin(BasePageTagAdmin):
    pass

 







admin.site.register(Page, PageAdmin)
admin.site.register(PageTag, PageTagAdmin)

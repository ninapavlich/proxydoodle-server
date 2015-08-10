from django.contrib import admin

from carbon.compounds.media.admin import ImageAdmin as BaseImageAdmin
from carbon.compounds.media.admin import MediaAdmin as BaseMediaAdmin
from carbon.compounds.media.admin import SecureMediaAdmin as BaseSecureMediaAdmin
from carbon.compounds.media.admin import MediaTagAdmin as BaseMediaTagAdmin

from .models import *
from .forms import *

class ImageAdmin(BaseImageAdmin):

    

    form = ImageAdminForm

    core_fields = (
        'title',
        ('image','preview'),
        ('square_crop', 'width_1200_wide_crop'),
       
        ('image_variants'),
        ('clean_filename_on_upload','allow_overwrite'),
        ('alt','use_png'),
        'credit',
        'caption',
        'tags'
    )
    

    meta_fields = (
        ('version'),
        ('created_date', 'created_by'),
        ('modified_date', 'modified_by'),
        'admin_note'
    )

    fieldsets = (
        ("Image", {
            'fields': core_fields,
        }),
        ("Meta", {
            'fields': meta_fields,
            'classes': ( 'grp-collapse grp-closed', )
        })
    )



class MediaAdmin(BaseMediaAdmin):
    pass

# class SecureMediaAdmin(BaseSecureMediaAdmin):
#     pass

class MediaTagAdmin(BaseMediaTagAdmin):
    pass    


admin.site.register(Image, ImageAdmin)
admin.site.register(Media, MediaAdmin)    
# admin.site.register(SecureMedia, SecureMediaAdmin)  
admin.site.register(MediaTag, MediaTagAdmin)        
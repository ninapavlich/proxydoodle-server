from django.db import models
from django.conf import settings

from carbon.atoms.models.abstract import VersionableAtom, OrderedItemAtom
from carbon.compounds.page.models import Page as BasePage
from carbon.compounds.page.models import PageTag as BasePageTag
from carbon.compounds.page.models import PageContentBlock as BasePageContentBlock
from carbon.compounds.media.models import Image as BaseImage

from imagekit import ImageSpec
from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from imagekit.admin import AdminThumbnail
from imagekit.processors import ResizeToFill, ResizeToFit

from proxydoodle.apps.media.models import Image


    
class Page(BasePage):
    default_template = 'page_base'
    @property
    def slides(self):
        return PageSlide.objects.filter(parent=self).order_by('order').select_related('slide_image')

    def get_page_content_blocks(self):
        blocks = PageContentBlock.objects.filter(parent=self).order_by('order')
        published = [block for block in blocks if block.is_published()]
        return published


class PageTag(BasePageTag):  
    default_template = 'page_tag'


class PageSlide(VersionableAtom, OrderedItemAtom):
    
    parent = models.ForeignKey('page.Page')

    slide_image = models.ForeignKey('media.Image', null=True, blank=True)

    link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['order']

class PageContentBlock(BasePageContentBlock):
    pass
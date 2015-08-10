from django.conf import settings
from django.contrib.sitemaps import Sitemap

from carbon.atoms.sitemap.content import SEOSitemap

from .models import Page,PageTag

class PageSitemap(SEOSitemap):    
    model = Page

class PageTagSitemap(SEOSitemap):
	model = PageTag
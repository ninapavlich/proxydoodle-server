from carbon.compounds.page.views import PageDetail as BasePageDetail
from carbon.compounds.page.views import PageTagView as BasePageTagView
from carbon.compounds.page.views import PageBlockView as BasePageBlockView

from .models import *


class PageDetail(BasePageBlockView, BasePageDetail):

    model = Page

class PageTagView(BasePageTagView):

    model = PageTag

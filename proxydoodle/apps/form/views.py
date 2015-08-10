from carbon.compounds.form.views import CreateFormEntryView as BaseCreateFormEntryView
from carbon.compounds.form.views import UpdateFormEntryView as BaseUpdateFormEntryView
from carbon.compounds.form.views import FormSubmittedView as BaseFormSubmittedView

from .models import *
from .forms import *

class CreateFormEntryView(BaseCreateFormEntryView):
    model = Form
    form_class = FormEntryForm

class UpdateFormEntryView(BaseUpdateFormEntryView):
    model = Form
    form_class = FormEntryForm
    form_entry_class = FormEntry


class FormSubmittedView(BaseFormSubmittedView):
	model = Form
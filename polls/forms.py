from django.forms.models import modelformset_factory
from .models import AnnouncedPuResults

pollingFormset = modelformset_factory(AnnouncedPuResults, exclude=(), extra=8)

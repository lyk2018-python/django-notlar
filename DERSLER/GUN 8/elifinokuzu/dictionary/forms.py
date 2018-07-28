from django import forms
from .models import LANGUAGE_CHOICES, EDGE_TYPE_CHOICES
from django.utils.translation import ugettext_lazy as _
from captcha.fields import ReCaptchaField

class SubmissionForm(forms.Form):
    source_language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES,
        label=_('Source Language'),
    )
    source_node = forms.CharField(
        help_text=_("Example: Elif in Turkish language"),
        max_length=255,
        label=_('Source Node'),
    )
    target_language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES,
        label=_('Target Language'),
    )
    target_node = forms.CharField(
        help_text=_("Example: Alpha in Ancient Greek"),
        max_length=255,
        label=_('Target Node'),
    )
    type_of_edge = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=EDGE_TYPE_CHOICES,
        label=_('Type of Edge'),
    )
    resource = forms.CharField(
        help_text=_("Example: Sevan Nişanyan's Elifin Öküzü"),
        max_length=255,
        label=_('Resource'),
    )
    captcha = ReCaptchaField()

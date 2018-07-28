from django.forms import ModelForm
from .models import Issue
from captcha.fields import ReCaptchaField
class ReportForm(ModelForm):
    class Meta:
        model = Issue
        fields = ['url',"explantation"]

    captcha = ReCaptchaField()
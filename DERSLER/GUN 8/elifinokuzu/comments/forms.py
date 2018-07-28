from django import forms
from .models import Comment_To_Node, Comment_To_Edge #Node, Edge
from captcha.fields import ReCaptchaField

class CommentFormForNode(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Comment_To_Node
        fields = ('text',)

class CommentFormForEdge(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Comment_To_Edge
        fields = ('text',)

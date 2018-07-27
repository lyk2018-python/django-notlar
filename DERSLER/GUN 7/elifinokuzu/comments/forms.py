from django import forms
from .models import Comment #Node, Edge

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
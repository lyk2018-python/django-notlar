from django import forms
from .models import LANGUAGE_CHOICES, EDGE_TYPE_CHOICES

class submission_form(forms.Form):
	source_language = forms.CharField(
		max_length=255,
		label='Source Language'
		)

	target_language = forms.CharField(
		max_length=255,
		label='Target Language'
		)
	
	source_node = forms.CharField(
		max_length=255,
		label='Source Node'
		)
	
	target_node = forms.CharField(
		max_length=255,
		label='Target Language'
		)

	type_of_edge = forms.CharField(
		max_length=255,
		label='Type of edge'
		)

	resource = forms.CharField(
		max_length=255,
		label='Resource'
		)
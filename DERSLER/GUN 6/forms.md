### Formlar
*forms.py* dosyası çalışması istenen app in içerisinde yaratılır ardından projeye uygun şekilde içeriği doldurulur.

```python
from django import forms
from .models import LANGUAGE_CHOICES, EDGE_TYPE_CHOICES


class submission_form(forms.Form):
	source_language = forms.ChoiceField(
		choices=LANGUAGE_CHOICES,
		label='Source Language'
		)

	source_node = forms.CharField(
		help_text="Example: Elif in Turkish language",
		max_length=255,
		label='Source Node'
		)
	
	target_language = forms.ChoiceField(
		choices=LANGUAGE_CHOICES,
		label='Target Language',
		)
	
	target_node = forms.CharField(
		help_text="Example: Alpha in Ancient Greek",
		max_length=255,
		label='Target Node'
		)

	type_of_edge = forms.ChoiceField(
		widget=forms.RadioSelect(),
		choices=EDGE_TYPE_CHOICES,
		label='Type of edge'
		)

	resource = forms.CharField(
		help_text="Example: Sevan Nişanyan's Elifin Öküzü",
		max_length=255,
		label='Resource'
		)
```
Ardından *views.py* a ve *urls.py* a gerekli alanlar eklenir;

*urls.py*
```python
		urlpatterns = [
	    path('', dictionary_views.home, name="home"),
	    path('about/', dictionary_views.about, name="about"),
	    path('support/', dictionary_views.support, name="support"),
	    path('node/<int:id>/', dictionary_views.node_detail, name="node_detail"),
	    path('admin/', admin.site.urls),
	    path('accounts/', include('django.contrib.auth.urls')),
	    path('accounts/signup', account_views.signup, name='signup'),
	    path('accounts/profile/', account_views.submit.dashboard, name='dashboard' ),
		path('submit/', dictionary_views.submit, name='submit') #THIS
	]
```
*views.py*
```python
	from forms import as submission_form
	from django.shortcuts import render, redirect
	from django.urls import reverse
def submit(request):
	if request.method == 'POST':
		form = submission_form(request.POST)
		if form.is_valid():
			source_node = Node.objects.create(
				name=form.cleaned_data['source_node'],
				language=form.cleaned_data['source_language']
				)
			target_node = Node.objects.create(
				name=form.cleaned_data['target_node'],
				language=form.cleaned_data['target_language']
				)
			type_of_edge = Edge.objects.create(
				source=source_node,
				destination=target_node,
				is_directed=False,
				type_of_edge=form.cleaned_data['type_of_edge'],
				resource=form.cleaned_data['resource'],
				)
			return redirect(reverse("node_detail", args=[source_node.id]))
	else:
		form = submission_form()
	return render(request, "submit.html", {'form': form})
```
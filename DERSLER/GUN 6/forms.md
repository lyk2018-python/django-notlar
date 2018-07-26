### Formlar
*forms.py* dosyası çalışması istenen app in içerisinde yaratılır ardından projeye uygun şekilde içeriği doldurulur.
```python
	from django import forms

	class submission_form(forms.Form):
		source_language = forms.CharField(
			max_length=255,
			label='Source Language',
			help_text='The language of origin word'
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
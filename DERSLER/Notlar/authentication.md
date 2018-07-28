### Authentication
#### Login
Django default authentication için *urls.py* sayfasına
```python
	from django.urls import path, include
	path('accounts/', include('django.contrib.auth.urls')),
```
eklenir
Ardından *login.html* sayfası eklenmesi gerekmektedir
```python
	{% extends 'base.html' %}
	{% block title %}Login{% endblock %}

	{% block content %}
	  <h2>Login</h2>
	  <form method="post">
	    {% csrf_token %}
	    {{ form.as_p }}
	    <button type="submit">Login</button>
	  </form>
	{% endblock %}	
```

Bir klasörü python paketine çevirmek için *__init__.py* eklemek gerekir

#### Register

```python
	{% extends 'base.html' %}

	{% block content %}
	  <h2>Sign up</h2>
	  <form method="post">
	    {% csrf_token %}
	    {{ form.as_p }}
	    <button type="submit">Sign up</button>
	  </form>
	{% endblock %}
```
```python
	from django.urls import path, include
	path('accounts/signup', account_views.signup, name='signup'),
```
#### Runtime da Pyhton debugger çalıştırmak için
Debug yapılması istenen satıra;
```python
	import pdb; pdb.set_trace()
```
yazılır ve
```python
	python manage.py runserver
```
ile proje çalıştırıldığında terminalde shell çalışır ve bu sayede debug yapılabilir.
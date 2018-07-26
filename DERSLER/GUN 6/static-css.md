### Base CSS Files
*settings.py* dosyasına *STATICFILES_DIRS* adlı array(liste) eklenir ardından içine
```python
		STATICFILES_DIRS = [
	    os.path.join(BASE_DIR, 'static'),
	]
```
eklenir.
Ardından istenen konuma css dosyası yaratılır ve istenilen şekilde doldurulur.
```css
* {
    font-family: Helvetica;
    /* Put your CSS here */
}
```
Daha sonra *base.html* e yada eklenmek istenilen html sayfasına *{% block css %}* şeklinde eklenir.
```html
	{% block css %}
	{% load static %}
	<link rel="stylesheet" href="{% static 'layout/styles/base.css'%}" type="text/css" />
	{% endblock %}
	...
```
### Base Templates
Base template başka bir html dosyasını base olarak inherit etmek için kullanılır

```python
{% block title %}
	YOUR-TITLE
{% endblock %}
{% extends "base_template.html" %}
	{% block body_block %}
		<h1>{{ node.name }}</h1>
		{% if incoming %}
			<h3>Incoming</h3>
			{% for edge in incoming %}
				{{ edge }} <br/>
			{% endfor %}
		{% endif %}
		{% if outgoing %}
			<h3>Outgoing</h3>
			{% for edge in outgoing %}
				{{ edge }} <br/>
			{% endfor %}
		{% endif %}
	{% endblock %}
```
*node_detail.html* dosyasının içeriğini başka bir html dosyası olan *base_template.html* dosyası içerisinde kullanabiliriz
```html
<!DOCTYPE html>
<html>
	<head>
	 	<meta charset="utf-8">
	 	<title>
	 		{% block title %}
 				Default Title
 			{% endblock %}
 		</title>
	</head>
	<body>
		{% block body_block %}
		{% endblock %}
	</body>
</html>
```
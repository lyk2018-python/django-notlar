### Models
Yaratılmak istenen model class şeklinde oluşturulur ve models.Model classından türetilir.
```python
	from django.db import models


	class Node(models.Model):
```
Ardından yaratılan class içerisi *CharField*, *ForeignKey*, *BooleanField* gibi fieldlar ile modellenir.
Admin panelinde eklenen objenin isminin görünmesi için *__str__* fonksiyonu(Java'daki *.toString()*) ezilir.
```python
	class Node(models.Model):
    name = models.CharField(max_length = 255)
    language =  models.CharField(
    	max_length=255,
    	choices=LANGUAGE_CHOICES
    )

    def __str__(self):
    	return self.name

class Edge(models.Model):
	source = models.ForeignKey(
		Node,
		related_name="incoming",
		on_delete=models.CASCADE,
	)
	destination = models.ForeignKey(
		Node,
		related_name="outgoing",
		on_delete=models.CASCADE,
	)
	is_directed = models.BooleanField()
	type_of_edge = models.CharField(
		max_length=255,
		choices=EDGE_TYPE_CHOICES
	)
	def __str__(self):
		if self.is_directed:
			arrow = "-->"
		else:
			arrow = "<->"
		return "%s:%s %s %s:%s" % (
			self.source.language,
			self.source.name.lower(),
			arrow,
			self.destination.language,
			self.destination.name.lower()
		)
```
Eklenen modelin Admin panelde görünmesi için *admim.py* dosyasına ekleme yapılır.
```python
	from django.contrib import admin
	from dictionary.models import Node,Edge


	admin.site.register(Node)
	admin.site.register(Edge)
```
Ardından eklenen modeller ve modellerde yapılan değişiklikler için 
```
	python manage.py makemigrations
	python manage.py migrate
```
yapılır.
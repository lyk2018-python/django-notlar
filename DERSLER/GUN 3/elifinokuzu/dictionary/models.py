from django.db import models


LANGUAGE_CHOICES = (
	("tr", "Turkish"),
	("fr", "French"),
	("de", "German"),
	("pl", "Polish"),
	("kr", "Kurdish"),
	("lt", "Latin"),
	("en", "English"),
	("es", "Spanish"),
)
class Node(models.Model):
    """
    Node (düğüm).
	The most base entity in the dictionary
    """
    name = models.CharField(max_length = 255)
    language =  models.CharField(
    	max_length = 255,
    	choices = LANGUAGE_CHOICES
    )
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
	("ar", "Arabic"),
)

EDGE_TYPE_CHOICES = (
	("derives_from", "Derives from"),
	("symbol_of", "Symbol of"),
	("compound_of", "Compound of"),
)

class Node(models.Model):
    """
    Node (düğüm).
	The most base entity in the dictionary
    """
    name = models.CharField(max_length = 255)
    language =  models.CharField(
    	max_length=255,
    	choices=LANGUAGE_CHOICES
    )

    def __str__(self):
    	return self.name

class Edge(models.Model):
	"""
	Edge (kenar)
	Holds the relationship between nodes
	"""
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
			arrow = '---[%s]-->' % self.type_of_edge
		else:
			arrow = "<--[%s]-->" % self.type_of_edge
		return '(%s:%s) %s (%s:%s)' % (
			self.source.language,
			self.source.name.lower(),
			arrow,
			self.destination.language,
			self.destination.name.lower()
		)
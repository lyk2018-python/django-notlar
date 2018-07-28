from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


LANGUAGE_CHOICES = (
    ('tr', _('Turkish')),
    ('fr', _('French')),
    ('gr', _('German')),
    ('pl', _('Polish')),
    ('kr', _('Kurdish')),
    ('lt', _('Latin')),
    ('en', _('English')),
    ('es', _('Spanish')),
    ('ar', _('Arabic')),
)

EDGE_TYPE_CHOICES = (
    ('derives_from', _('Derives from')),
    ('symbol_of', _('Symbol of')),
    ('compound_of', _('Compound of')),
)


class Node(models.Model):
    """
    Node (düğüm)
    The most base entity in the dictionary
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255, unique=True)
    language = models.CharField(
        max_length=255,
        choices=LANGUAGE_CHOICES
    )

    def __str__(self):
        return self.name


class Edge(models.Model):
    """
    Holds the relationships between nodes.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
    )
    source = models.ForeignKey(
        Node,
        related_name='incoming',
        on_delete=models.CASCADE,
    )
    destination = models.ForeignKey(
        Node,
        related_name='outgoing',
        on_delete=models.CASCADE,
    )
    is_directed = models.BooleanField()
    resource = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    type_of_edge = models.CharField(
        max_length=255,
        choices=EDGE_TYPE_CHOICES
    )

    def __str__(self):
        if self.is_directed:
            arrow = '---[%s]-->' % self.type_of_edge
        else:
            arrow = '<--[%s]-->' % self.type_of_edge

        return '(%s:%s) %s (%s:%s)' % (
            self.source.language,
            self.source.name.lower(),
            arrow,
            self.destination.language,
            self.destination.name.lower(),
        )

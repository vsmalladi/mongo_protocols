from django.db import models
from django.core.urlresolvers import reverse

from djangotoolbox.fields import ListField, EmbeddedModelField

#Protocol Types
PROTOCOL_TYPES = (
    ('GP', 'Growth Protocol'),
    ('TP', 'Treatment Protocol'),
    ('IP', 'Input prep Protocol'),
    ('TP', 'Technology Protocol')
)

class Protocol(models.Model):
    created_at = models.DateTimeField(auto_now_add = True, db_index= True)
    name = models.CharField(verbose_name = "Protocol Name", max_length = 255)
    slug = models.SlugField()
    protocol_type = models.CharField(verbose_name = "Category", max_length = 2, choices = PROTOCOL_TYPES)
    description = models.TextField()
    author = models.CharField(verbose_name = "Name", max_length = 255)
    sections = ListField(EmbeddedModelField('Section'), editable = False)

    def get_absolute_url(self):
        return reverse('protocol', kwargs=("slug", self.slug))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-name"]

class Section(models.Model):
    title = models.CharField(verbose_name = "Section Title", max_length=255)
    section_no = models.IntegerField(verbose_name = "Section Number", db_index = True)
    description = models.TextField()
    steps = ListField(EmbeddedModelField('Step'), editable = False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-section_no"]

class Step(models.Model):
    step_no = models.IntegerField(verbose_name = "Step Number")
    description = models.TextField()


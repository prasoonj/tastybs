from django.db import models
#from tastypie.utils.timezone import now
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class Activity(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    #time = models.DateTimeField(default=now)
    #tags = ListField(StringField)
    #comments = ListField(EmbeddedDocumentField(comment))
    #id =
    #audit = EmbeddedDocumentField(Audit)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        # For automatic slug generation.
        if not self.slug:
            self.slug = slugify(self.title)[:50]
        return super(Entry, self).save(*args, **kwargs)

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Sponsor(models.Model):
    """
        Sponsor model
    """
    name = models.CharField(_('Name'), max_length=200)
    slug = models.SlugField()
    pub_date = models.DateField(_('Date Published'))

    def __unicode__(self):
        return u'%s' % self.name


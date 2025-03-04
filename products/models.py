from django.db import models
from django.utils.translation import ugettext_lazy as _

class Catagory(models.Model):
    parent = models.ForeignKey('self',verbose_name=_('parent'),blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(_('name'),max_length=50)
    descreption = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='catagories')
    is_enable = models.BooleanField(_('is_enable'),default=True)
    created_time = models.DateTimeField(_('created_time'),auto_now_add=True)
    update_time =models.DateTimeField(_('update_time'),auto_now=True)
    class Meta:
        db_table = 'catagoreis'
        verbos_name  = _('catagory')
        verbose_name_plural = _('catagories')
    
class Product(models.Model):
    pass

class File(models.Model):
    pass


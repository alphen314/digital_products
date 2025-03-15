from django.db import models
from django.utils.translation import gettext_lazy as _


class Catagory(models.Model):
    parent = models.ForeignKey('self',verbose_name=_('parent'),blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(_('name'),max_length=50)
    descreption = models.TextField(_('descreption'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='catagories')
    is_enable = models.BooleanField(_('is_enable'),default=True)
    created_time = models.DateTimeField(_('created_time'),auto_now_add=True)
    update_time =models.DateTimeField(_('update_time'),auto_now=True)
    class Meta:
        db_table = 'catagoris'
        verbose_name  = _('catagory')
        verbose_name_plural = _('catagories')
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(_('title'),max_length=50)
    descreption  = models.TextField(_('descreption'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='products/')
    is_enable = models.BooleanField(_('is_enable'),default=True)
    catagories = models.ManyToManyField('catagory',verbose_name= _('catagories'),blank=True)
    created_time = models.DateTimeField(_('created_time'),auto_now_add=True)
    update_time =models.DateTimeField(_('update_time'),auto_now=True)
    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')
    def __str__(self):
        return self.title


class File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 3
    FILE_TYPES = (
        (FILE_AUDIO,_('audio')),
        (FILE_VIDEO,_('video')),
        (FILE_PDF,_('pdf')),
    )
    product = models.ForeignKey('Product',verbose_name=_('product'),related_name='files',on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length=50)
    file_type = models.PositiveSmallIntegerField(_('file_type'),choices=FILE_TYPES)
    file = models.FileField(_('file'),upload_to='files/%Y/%m/%d/')
    is_enable = models.BooleanField(_('is_enable'),default=True)
    created_time = models.DateTimeField(_('created_time'),auto_now_add=True)
    update_time =models.DateTimeField(_('update_time'),auto_now=True)
    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')
    def __str__(self):
        return self.title

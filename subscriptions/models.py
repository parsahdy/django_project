from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User
from utils.validators import validate_sku


class Package(models.Model):
    title = models.CharField(_('title'), max_length=50)
    sku = models.CharField(_('stock keeping unit'), max_length=20, validators=[validate_sku], db_index=True)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(('avatar'), blank=True, upload_to='packages/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    price = models.PositiveBigIntegerField(_('price'))
    duration = models.DurationField(_('duration'), blank=True, null=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)


    class Meta:
        db_table = 'packages'
        verbose_name = _('package')
        verbose_name_plural = _('packages')



class Subscription(models.Model):
    user = models.ForeignKey('users.User', related_name='%(class)s', on_delete=models.CASCADE)
    package = models.ForeignKey(Package, related_name='%(class)s', on_delete=models.CASCADE)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    expired_time = models.DateTimeField(_('expire time'), blank=True, null=True)

    
    class Meta:
        db_table = 'subscriptions'
        verbose_name = _('subscription')
        verbose_name_plural = _('subscriptions')
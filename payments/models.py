from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.validators import validate_phone_number
from subscriptions.models import Package

class Gateway(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='getaway/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    #credentials = models.TextField(_('credentials'), blank=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)


    class Meta:
        db_table = 'getways'
        verbose_name = _('getway')
        verbose_name_plural = _('getways')


class Payment(models.Model):
    STATUS_VOID = 0
    STATUS_PAID = 10
    STATUS_ERROR = 20
    STATUS_CANCELED = 30
    STATUS_REFUNDED = 31
    STATUS_CHOICES = (
        (STATUS_VOID, _('Void')),
        (STATUS_PAID, _('Paid')),
        (STATUS_ERROR, _('Error')),
        (STATUS_CANCELED, _('void')),
        (STATUS_REFUNDED, _('void')),
    )

    STATUS_TRANSLATIONS = {
        STATUS_VOID: _('Payment could not be processed.'),
        STATUS_PAID: _('Payment successful.'),
        STATUS_ERROR: _('Payment has encountered an error. Our technical team will check it.'),
        STATUS_CANCELED: _('Payment canceled by user.'),
        STATUS_REFUNDED: _('This payment has been refunded.'),
    }


    user = models.ForeignKey('users.User',verbose_name=('user'), related_name='%(class)s', on_delete=models.CASCADE)
    package = models.ForeignKey('subscriptions package',verbose_name=('package'), related_name='%(class)s', on_delete=models.CASCADE)
    getway = models.ForeignKey(Gateway,verbose_name=('gateway'), related_name='%(class)s', on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField(_('price'), default=0)
    status = models.PositiveIntegerField(_('price'), choices=STATUS_CHOICES, default=STATUS_VOID, db_index=True)
    device_uuid = models.CharField(_('device uuid'), max_length=40, blank=True)
    token = models.CharField()
    phone_number = models.BigIntegerField(_('phone number'), validators=[validate_phone_number], db_index=True)
    consumed_code = models.PositiveIntegerField(_('consumed refrence code'), null=True, db_index=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True, db_index=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)


    class Meta:
        db_table = 'payments'
        verbose_name = _('payment')
        verbose_name_plural = _('payments')
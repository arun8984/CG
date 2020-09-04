from django.db import models
from django.utils.translation import gettext_lazy as _

class Currencies(models.Model):
    CurrencyCode = models.CharField(_('Currency Code'),primary_key=True,max_length=3)
    CurrencyName = models.CharField(_('Currence Name'),max_length=100,blank=False,null=False)
    Currency_Symbol = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = _('Currencies')
        verbose_name_plural = _('Currencies')
    
    def __str__(self):
        return str(self.CurrencyCode + ' - ' + self.CurrencyName)

class Services(models.Model):
    
    ServiceID = models.AutoField(primary_key=True)
    ServiceName = models.CharField(max_length=50,blank=False, null=False,verbose_name=_('Service Name'))
    Enabled = models.BooleanField(default=False,blank=False, null=False,verbose_name=_('Enabled'))
        
    class Meta:
        verbose_name = _('Services')
        verbose_name_plural = _('Services')
    
    def __str__(self):
        return self.ServiceName
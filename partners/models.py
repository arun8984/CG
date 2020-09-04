import eav
from django.db import models
from enum import IntEnum
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from website.models import Services
from os import path
from uuid import uuid4
from django.utils.html import mark_safe

class RemittanceMethods(IntEnum):
    BANK=1
    CARD=2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class PartnerTypes(IntEnum):
    INDIVIDUAL=1
    COMPANY=2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class PaymentMethods(IntEnum):
    CASH=1
    ONLINE=2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class Partners(models.Model):
    FirstName = models.CharField(max_length=100,blank=False, null=False,verbose_name=_('First Name'))
    LastName = models.CharField(max_length=50,blank=False, null=False,verbose_name=_('Last Name'))
    Email = models.EmailField(verbose_name=_('Email address'),max_length=255,blank=False,null=False)
    Phone = PhoneNumberField(blank=False, null=False)
    AccountType = models.PositiveSmallIntegerField(_('Account Type'),choices=PartnerTypes.choices(),blank=False, null=False)
    BusinessName = models.CharField(max_length=200,blank=True, null=True,verbose_name=_('Business Name'))
    RegistertionNo = models.CharField(max_length=200,blank=True, null=True,verbose_name=_('Registration No'))
    Address1 = models.CharField(max_length=255,blank=False, null=False,verbose_name=_('Address 1'))
    Address2 = models.CharField(max_length=255,blank=True, null=True,verbose_name=_('Address 2'))
    City = models.CharField(max_length=255,blank=False, null=False,verbose_name=_('City'))
    State = models.CharField(max_length=255,blank=False, null=False,verbose_name=_('State/County'))
    Country = CountryField(blank=False, null=False)
    Remittance = models.PositiveSmallIntegerField(_('Remittance Method'),choices=RemittanceMethods.choices(),blank=False, null=False)
    Verified = models.BooleanField(_('Verified'),blank=False,null=False,default=False,db_index=True)
    Enabled = models.BooleanField(_('Enabled'),blank=False,null=False,default=False,db_index=True)

    class Meta:
        verbose_name = _('Partners')
        verbose_name_plural = _('Partners')
    
    def __str__(self):
        return self.FirstName + ' ' + self.LastName if self.AccountType == PartnerTypes.INDIVIDUAL else self.BusinessName

class Profiles(models.Model):
    Partner = models.ForeignKey(Partners,on_delete=models.PROTECT,related_name='partner_profiles',null=False,blank=False,db_index=True)
    DisplayName = models.CharField(max_length=255,blank=False, null=False,verbose_name=_('Display Name'))
    Services = models.ManyToManyField(Services,related_name='profile_services',verbose_name=_('Services Offered'),db_index=True)
    ServiceLocation = models.CharField(max_length=255,blank=False, null=False,verbose_name=_('Service Location'),db_index=True)
    PaymentMethod = models.PositiveSmallIntegerField(_('Payment Method'),choices=PaymentMethods.choices(),blank=False, null=False)
    Enabled = models.BooleanField(_('Enabled'),blank=False,null=False,default=False,db_index=True)

    class Meta:
        verbose_name = _('Profiles')
        verbose_name_plural = _('Profiles')
    
    def __str__(self):
        return self.DisplayName

def rename_upload_path(instance, filename):

    if type(instance)==type(ProfileImages()):
        upload_to = 'profile/images'
    #elif type(instance)==type(PageContent()):
    #    upload_to = 'cmsimg'        
    #elif type(instance)==type(PageBanner()):
    #    upload_to = 'bannerimg'
        
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}-{}.{}'.format(instance.pk,uuid4().hex, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return path.join(upload_to, filename)

class ProfileImages(models.Model):
    Profile = models.ForeignKey(Profiles, related_name='images',on_delete=models.DO_NOTHING,verbose_name=_('Profile'),db_index=True)
    Image = models.ImageField(upload_to=rename_upload_path,blank=False,null=False)

    class Meta:
        verbose_name = _('Profile Images')
        verbose_name_plural = _('Profile Images')
    
    def __str__(self):
        return self.Profile.DisplayName
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.Image.url))

    image_tag.short_description = 'Image'

eav.register(Profiles)
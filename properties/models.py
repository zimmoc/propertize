import uuid
import datetime

from django.db import models
from tenants.models import Tenant
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

# Create your models here.

User = get_user_model()


class Property(models.Model):
    property_id = models.AutoField(unique=True, primary_key=True)
    landlord = models.ForeignKey(User, on_delete=models.PROTECT, related_name="properties")
    assigned_contractor = models.ManyToManyField(User, related_name="assigned_contractor", blank=True)
    address = models.CharField(max_length=150)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    featured_image = CloudinaryField('image', default='placeholder')
    details = models.TextField(blank=True)

    def __str__(self):
            return self.name


class InvitationCode(models.Model):
    """
    Instead of creating a proxy im just keeping the model here for now
    """
    id = models.AutoField(primary_key=True, unique=True)
    tenant_name = models.CharField(max_length=70, default="Jane Doe", verbose_name="Tenant")
    code = models.CharField(max_length=5, unique=True, blank=True)
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE, related_name='invitation_codes')
    rent_amount = models.FloatField(default=0)
    lease_end = models.DateField(default=datetime.date.today)
    next_rent_due = models.DateField(default=datetime.date.today)
    apartment = models.CharField(max_length=10, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.tenant_name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.code = self.generate_unique_code()
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        return str(uuid.uuid4().hex)[:5]


class PropertyNotice(models.Model):
     notice_id = models.AutoField(primary_key=True, unique=True)
     posted_at = models.DateTimeField(auto_now_add=True)
     title = models.CharField(max_length=100)
     body = models.TextField()
     property = models.ForeignKey('properties.Property', on_delete=models.CASCADE, related_name='property_notice')
     posted_by = models.CharField(max_length=100)
     important = models.BooleanField(default=False)

     def __str__(self):
        return self.title


class ProxyTenant(Tenant):
     """ 
     This acts as a proxy for the tenants app model Tenant, 
     This is done to group tenants with properties in admin dashboard
     """
     class Meta:
          proxy = True
          verbose_name = Tenant._meta.verbose_name
          verbose_name_plural = Tenant._meta.verbose_name_plural

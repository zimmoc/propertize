from datetime import datetime, timedelta

from django.urls import reverse
from django.test import TestCase
from tenants.models import Tenant
from properties.models import Property
from django.contrib.auth import get_user_model

# Create your tests here.

class TestHomeViews(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user_landlord = User.objects.create_superuser(
            username="landlordUser",
            password="landlordPassword",
            email="landlord@test.com",
            first_name='Landlord',
            last_name='User',
            role=1
        )

        self.user_contractor = User.objects.create_superuser(
            username="contractorUser",
            password="contractorPassword",
            email="contractor@test.com",
            first_name='Contractor',
            last_name='User',
            role=2
        )

        self.property = Property.objects.create(landlord=self.user_landlord, address='420 Test St', zip_code=1337, city='Test City', name='Test Property')

        self.user_tenant = User.objects.create_superuser(
            username="tenantUser",
            password="tenantPassword",
            email="tenant@test.com",
            first_name='Tenant',
            last_name='User',
            role=3,
            assigned_property=self.property
        )

        self.tenant = Tenant.objects.create(
            resident=self.user_tenant,
            lease_end=datetime.now().date() + timedelta(days=365),
            rent_amount=1000,
            outstanding_rent=0,
            overdue_fee=50,
            next_rent_due=datetime.now().date(),
            apartment='1A',
            is_active=True
        )

        self.user_none = User.objects.create_superuser(
            username="noneUser",
            password="nonePassword",
            email="none@test.com",
            first_name='None',
            last_name='User',
            role=0
        )

    def test_render_dashboard_as_landlord(self):
        """ Test that it renders Landlord dashboard if you are a landlord """
        self.client.login(
            username="landlordUser", password="landlordPassword")
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"landlord_confirm", response.content)

    def test_render_dashboard_as_contractor(self):
        """ Test that it renders Contractor dashboard if you are a Contractor """
        self.client.login(
            username="contractorUser", password="contractorPassword")
        response = self.client.get(reverse('home'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(f'{self.user_contractor.username}', response.content.decode())

    def test_render_dashboard_as_tenant(self):
        """ Test that it renders tenant dashboard if you are a tenant """
        
        self.client.login(
            username="tenantUser", password="tenantPassword")
        response = self.client.get(reverse('home'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user_tenant.username, response.content.decode())

    def test_render_dashboard_as_none(self):
        """ Test that it renders none dashboard if you are a none """
        self.client.login(
            username="noneUser", password="nonePassword")
        response = self.client.get(reverse('home'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"invitation_code", response.content)

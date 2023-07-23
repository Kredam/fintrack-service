import unittest
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.serializers import ValidationError

class AccountTests(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='username', password='Pas$w0rd')
        self.client.login(username="username", password="Pas$w0rd")
        return super().setUp()

    # Create your tests here.
    def test_empty_card_number(self) -> None:
        payload = {
            "expire": "2034-03-10",
            "type": 'CRD',
            "holder": self.user.pk,
            "balance": 100000,
            "description": "Mastercard",
        }
        self.client.post('/api/v1/account/', data=payload)
        self.assertRaisesMessage(expected_exception=ValidationError, expected_message="Credit or Debit cards must have a number")

    def test_delete_other_user_acccount(self) -> None:
        pass

    def test_delete_user_account(self) -> None:
        pass

    def test_update_user_account(self) -> None:
        payload = {
            "expire": "2035-03-10",
            "type": 'RD',
            "holder": self.user.pk,
            "number": 12345678912345678,
            "balance": 100000,
            "description": "Mastercard",
        }
        response = self.client.patch('/acount/', data=payload)
        self.assertDictEqual(payload, response)

    def test_update_other_user_account(self) -> None:
        pass

    def test_create_accont(self) -> None:
        payload = {
            "expire": "2035-03-10",
            "type": 'RD',
            "holder": self.user.pk,
            "number": 12345678912345678,
            "balance": 100000,
            "description": "Mastercard",
        }
        response = self.client.post('/account/', data=payload)
        self.assertEqual(response.status_code, 200)
    
    def test_past_expiration_date(self) -> None:
        payload = {
            "expire": "2015-03-10",
            "type": 'CRD',
            "holder": self.user.pk,
            "number": 12345678912345678,
            "balance": 100000,
            "description": "Mastercard",
        }
        response = self.client.post('/account/', data=payload)
        self.assertEquals(response.status_code, 400)
    
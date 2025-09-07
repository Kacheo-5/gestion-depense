from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Expense


class ExpenseAPITest(APITestCase):
	def setUp(self):
		self.list_url = reverse('expense-list')
		self.expense = Expense.objects.create(
			expense_type='Carburant',
			date='2025-09-01',
			quantity=50.0,
			amount=75000.00,
		)

	def test_list_expenses(self):
		resp = self.client.get(self.list_url)
		self.assertEqual(resp.status_code, status.HTTP_200_OK)
		self.assertGreaterEqual(len(resp.data), 1)

	def test_create_expense(self):
		payload = {
			'expense_type': 'Huile',
			'date': '2025-09-02',
			'quantity': '5.00',
			'amount': '15000.00',
		}
		resp = self.client.post(self.list_url, payload, format='json')
		self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Expense.objects.count(), 2)

	def test_retrieve_update_delete_expense(self):
		detail_url = reverse('expense-detail', args=[self.expense.id])
		# retrieve
		resp = self.client.get(detail_url)
		self.assertEqual(resp.status_code, status.HTTP_200_OK)
		# update
		resp = self.client.patch(detail_url, {'amount': '70000.00'}, format='json')
		self.assertEqual(resp.status_code, status.HTTP_200_OK)
		self.expense.refresh_from_db()
		self.assertEqual(str(self.expense.amount), '70000.00')
		# delete
		resp = self.client.delete(detail_url)
		self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
		self.assertFalse(Expense.objects.filter(id=self.expense.id).exists())


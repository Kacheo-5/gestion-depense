from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from .models import Expense
from .serializer import ExpenseSerializer
from . import services


class ExpenseViewSet(viewsets.ViewSet):
	"""CRUD API for Expense using a service layer"""
	filter_backends = [filters.SearchFilter, filters.OrderingFilter]
	search_fields = ['expense_type']
	ordering_fields = ['date', 'amount', 'created_at']

	def list(self, request):
		qs = services.list_expenses()
		serializer = ExpenseSerializer(qs, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		obj = services.get_expense(pk)
		if not obj:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = ExpenseSerializer(obj)
		return Response(serializer.data)

	def create(self, request):
		serializer = ExpenseSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		obj = services.create_expense(serializer.validated_data)
		return Response(ExpenseSerializer(obj).data, status=status.HTTP_201_CREATED)

	def partial_update(self, request, pk=None):
		obj = services.get_expense(pk)
		if not obj:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = ExpenseSerializer(obj, data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		obj = services.update_expense(obj, serializer.validated_data)
		return Response(ExpenseSerializer(obj).data)

	def destroy(self, request, pk=None):
		obj = services.get_expense(pk)
		if not obj:
			return Response(status=status.HTTP_404_NOT_FOUND)
		services.delete_expense(obj)
		return Response(status=status.HTTP_204_NO_CONTENT)



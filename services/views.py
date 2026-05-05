from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from .models import User, Category, Service, Employee, Order, Payment, Review, Message
from .serializers import (
    UserSerializer, CategorySerializer, ServiceSerializer,
    EmployeeSerializer, OrderSerializer, PaymentSerializer,
    ReviewSerializer, MessageSerializer
)


@extend_schema(tags=['Users'])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


@extend_schema(tags=['Categories'])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @extend_schema(summary="Отримати всі активні категорії")
    @action(detail=False, methods=['get'], url_path='active')
    def active(self, request):
        active = Category.objects.filter(is_active=True)
        serializer = self.get_serializer(active, many=True)
        return Response(serializer.data)


@extend_schema(tags=['Services'])
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    @extend_schema(summary="Отримати всі активні послуги")
    @action(detail=False, methods=['get'], url_path='active')
    def active(self, request):
        active = Service.objects.filter(status='active')
        serializer = self.get_serializer(active, many=True)
        return Response(serializer.data)


@extend_schema(tags=['Employees'])
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @extend_schema(summary="Отримати доступних співробітників")
    @action(detail=False, methods=['get'], url_path='available')
    def available(self, request):
        available = Employee.objects.filter(is_available=True)
        serializer = self.get_serializer(available, many=True)
        return Response(serializer.data)


@extend_schema(tags=['Orders'])
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @extend_schema(summary="Отримати замовлення за статусом")
    @action(detail=False, methods=['get'], url_path='by-status/(?P<status>[^/.]+)')
    def by_status(self, request, status=None):
        orders = Order.objects.filter(status=status)
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)


@extend_schema(tags=['Payments'])
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


@extend_schema(tags=['Reviews'])
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    @extend_schema(summary="Отримати видимі відгуки")
    @action(detail=False, methods=['get'], url_path='visible')
    def visible(self, request):
        visible = Review.objects.filter(is_visible=True)
        serializer = self.get_serializer(visible, many=True)
        return Response(serializer.data)


@extend_schema(tags=['Messages'])
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @extend_schema(summary="Отримати непрочитані повідомлення")
    @action(detail=False, methods=['get'], url_path='unread')
    def unread(self, request):
        unread = Message.objects.filter(is_read=False)
        serializer = self.get_serializer(unread, many=True)
        return Response(serializer.data)

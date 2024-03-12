from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import ProductListSerializer, ProductDetailsSerializer
from main.models import Product


@api_view(['GET'])
def products_list_view():
    """"реализуйте получение всех товаров из БД
    реализуйте сериализацию полученных данных
    отдайте отсериализованные данные в Response"""

    products_list = Product.objects.all()
    ser = ProductListSerializer(products_list, many=True)
    return Response(ser.data)


class ProductDetailsView(APIView):
    def get(self, product_id):
        """реализуйте получение товара по id, если его нет, то выдайте 404
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""

        qs = Product.objects.get(product_id, 'ошибка 404')
        ser = ProductDetailsSerializer(qs, many=True)
        return Response(ser.data)

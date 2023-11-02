from django.shortcuts import render
# from .models import Car
# from .serializers import CarSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Car, Brand
from django.forms import model_to_dict


# Create your views here.
class CarsAPIView(APIView):
    def get(self, request):
        lst = Car.objects.all().values()
        return Response({'posts': list(lst)})
    def post(self, request):
        brands_name = request.data['brands']
        year = request.data['year']
        
        # Получение объекта Brand по имени
        try:
            brand = Brand.objects.get(name=brands_name)
        except Brand.DoesNotExist:
            # Если объект Brand не найден, создаем новый
            brand = Brand.objects.create(name=brands_name)

        
        # Создание объекта Car с использованием объекта brand и идентификатора cat_id
        post_new = Car.objects.create(brands=brand, year=year,)
        
        return Response({'post': model_to_dict(post_new)})

# class CarsAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
from django.shortcuts import render

from rest_framework import serializers
from rest_framework.response import Response


from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework import viewsets

from rest_framework import filters
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import DroneCategory,Drones,Orders,Features
from .serializers import DroneCategorySerializer,DronesSerializer,OrderSerializer,FeatureSerializer
from django_filters.rest_framework import DjangoFilterBackend



class DroneSearchListView(generics.ListAPIView):
    queryset = Drones.objects.all()
    serializer_class = DronesSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ['title','brand','categories__title']

"""----ALL ABOUT CATEGORY START----"""
"""----GET CATEGORY ----"""

@api_view(['GET'])
def get_category(request):
    myexample = DroneCategory.objects.all()
    serializer = DroneCategorySerializer(myexample, many=True)
    return Response(serializer.data)

"""----CREATE CATEGORY ----"""

@api_view(['POST'])
def create_category(request):
    data = request.data    
    title=data.get('title')    
    query = DroneCategory.objects.create(title=title)
    query.save()    
    return Response({'message': 'The category is created!'})

"""----ALL ABOUT CATEGORY END----"""


"""----ALL ABOUT PRODUCTS START----"""

"""----GET ALL PRODUCTS----"""

@api_view(['GET'])
@permission_classes([AllowAny])
def get_drones(request):
    myexampledrone = Drones.objects.all()
    serializer = DronesSerializer(myexampledrone, many=True)
    return Response(serializer.data)

"""----GET PRODUCT----"""

@api_view(['GET'])
def get_drone(request, slug):
    try:
        
        queryset = Drones.objects.filter(slug=slug).order_by('id') 

    except Drones.DoesNotExist:
        return Response(
            {
              'errors':{'code':404, 'message':'Böyle bir çalışma bulunamadı.'}
                },
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method=='GET':
        drone_serializer = DronesSerializer(queryset, many=True)
        data = {
        'drone': drone_serializer.data,
        
        }
        return Response(data)


"""----CREATE PRODUCT----"""

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_drone(request):
    data = request.data    
    title=data.get('title')  
    brand=data.get('brand')  
    quantity=data.get('quantity')
    description=data.get('description')
    categories=data.get('categories')
    image=data.get('image')
    print(categories)

    categoryProfile=DroneCategory.objects.filter(title=categories).first()

    
    query = Drones.objects.create(title=title,brand=brand,quantity=quantity,categories=categoryProfile,description=description,image=image)
    
    query.save()    
    return Response({'message': 'The product is created!'})

"""----UPDATE PRODUCT----"""

@api_view(['POST'])
@permission_classes([IsAdminUser])
def update_drone(request,slug):
    
    data = request.data    
    title=data.get('title')  
    brand=data.get('brand')  
    quantity=data.get('quantity')
    description=data.get('description')
    categories=data.get('categories')   
    
    
    

    profile1=DroneCategory.objects.filter(title=categories).first()

    query =Drones.objects.filter(slug=slug).update(title=title,brand=brand,quantity=quantity,categories=profile1,description=description)
    
    
       
    return Response({'message': 'The product is edited!'})

"""----DELETE PRODUCT----"""

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_drone(request, slug):
    try:        
        queryset = Drones.objects.filter(slug=slug).order_by('id') 

    except Drones.DoesNotExist:
        return Response(
            {
              'errors':{'code':404, 'message':'Böyle bir çalışma bulunamadı.'}
                },
            status=status.HTTP_404_NOT_FOUND)
    
 
    if request.method == 'DELETE': 
        queryset.delete() 
        return 
    

"""----ALL ABOUT PRODUCTS END----"""



"""----ALL ABOUT ORDERS START----"""
"""----GET ALL ORDERS ----"""

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_orders(request):
    myorder = Orders.objects.all()
    serializer = OrderSerializer(myorder, many=True)
    return Response(serializer.data)

"""----GET USERS ORDER ----"""

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order_user(request):
    try:       
        
        queryset = Orders.objects.filter(user=request.user.id).order_by('id')         

    except Orders.DoesNotExist:
        return Response(
            {
              'errors':{'code':404, 'message':'Böyle bir çalışma bulunamadı.'}
                },
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method=='GET':
        order_serializer = OrderSerializer(queryset, many=True)
        data = {
        'userOrders': order_serializer.data,
        
        }
        return Response(data)

"""----GET ORDER ----"""

@api_view(['GET'])
def get_order(request, id):
    try:
        
        
        queryset = Orders.objects.filter(id=id).order_by('id') 

    except Orders.DoesNotExist:
        return Response(
            {
              'errors':{'code':404, 'message':'Böyle bir çalışma bulunamadı.'}
                },
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method=='GET':
        order_serializer = OrderSerializer(queryset, many=True)
        data = {
        'order': order_serializer.data,
        
        }
        return Response(data)

"""----CREATE ORDER ----"""

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    
    data = request.data    
    title=data.get('title')
    adress=data.get('adress')
    quantity=data.get('quantity')
    start_date=data.get('start_date')
    end_date=data.get('end_date')     
    
    zone=data.get('drone')
    
    print(zone)
    

    dronsProfile=Drones.objects.get(title=zone)

    
    query = Orders.objects.create(title=title,drone=dronsProfile,adress=adress,quantity=quantity,start_date=start_date,end_date=end_date,user=request.user)
    
    query.save()    
    return Response({'message': 'The order is created!'})



"""----CHECK ORDER STATUS----"""

class PostStatusAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=OrderSerializer
    lookup_field="id"
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Orders.objects.all() 
    

"""----ALL ABOUT ORDERS END----"""











"""----ALL ABOUT FEATURES START----"""
"""----GET ALL FEATURES----"""

@api_view(['GET'])
def get_features(request):
    myfeature = Features.objects.all()
    serializer = FeatureSerializer(myfeature, many=True)
    return Response(serializer.data)

"""----GET FEATURE----"""

@api_view(['GET'])
def get_feature(request, slug):
    try:
        detail = get_object_or_404(Drones, slug=slug)
        queryset = Features.objects.filter(drone=detail).order_by('id') 

    except Features.DoesNotExist:
        return Response(
            {
              'errors':{'code':404, 'message':'Böyle bir çalışma bulunamadı.'}
                },
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method=='GET':
        feature_serializer = FeatureSerializer(queryset, many=True)
        data = {
        'feature': feature_serializer.data,
        
        }
        return Response(data)

"""----CREATE FEATURE----"""

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_feature(request):
    data = request.data    
    title=data.get('title')       
    zone=data.get('drone')
    description=data.get('description')   
    

    droneProfile=Drones.objects.get(title=zone)
    
    query = Features.objects.create(title=title,drone=droneProfile,description=description)
    
    query.save()    
    return Response({'message': 'The feature is created!'})


"""----ALL ABOUT FEATURES END----"""
from rest_framework import serializers
from .models import DroneCategory,Drones,Orders,Features

class DroneCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneCategory
        fields = ('id', 'title', 'slug','created_at')

class DronesSerializer(serializers.HyperlinkedModelSerializer):
    categories = serializers.SerializerMethodField('get_categories')
    def get_categories(self, obj):
        return obj.categories.title
    class Meta:
        model = Drones
        fields = ('id', 'title', 'slug', 'image','brand','quantity','description','categories')



class OrderSerializer(serializers.ModelSerializer):
    drone = serializers.SerializerMethodField('get_drone')
    user = serializers.SerializerMethodField('get_user')
    def get_drone(self, obj):
        return obj.drone.title
    
    def get_user(self, obj):
        return obj.user.id
    
    class Meta:
        model = Orders
        fields = ('id', 'title', 'adress', 'drone','user','status','start_date','end_date','quantity','created_at')

class FeatureSerializer(serializers.ModelSerializer):
    drone = serializers.SerializerMethodField('get_drone')
    def get_drone(self, obj):
        return obj.drone.title
    class Meta:
        model = Features
        fields = ('id', 'title', 'description', 'drone')



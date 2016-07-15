from django.contrib.auth.models import User

from rest_framework import serializers
from places.models import Category, Place


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place

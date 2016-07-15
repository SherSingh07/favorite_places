from django.contrib.auth.models import User

from rest_framework import serializers
from places.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
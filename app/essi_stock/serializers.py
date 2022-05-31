from rest_framework import serializers
from .models import CategoriteLevelTwo, Item, CategoriteLevelOne, Categorite


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'marque', 'reference','image', 'price']


class CategoryLevelTwoSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only = True)
    class Meta:
        model = CategoriteLevelTwo
        fields = ['id', 'name', 'items']


class CategoryLevelOneSerializer(serializers.ModelSerializer):
    categorites_level_two = CategoryLevelTwoSerializer(many=True, read_only=True)
    class Meta:
        model = CategoriteLevelOne
        fields = ['id', 'name', 'categorites_level_two']


class CategorySerializer(serializers.ModelSerializer):
    categorites_level_one = CategoryLevelOneSerializer(many = True, read_only = True)
    class Meta:
        model = Categorite
        fields = ['id', 'name', 'icon', 'categorites_level_one']
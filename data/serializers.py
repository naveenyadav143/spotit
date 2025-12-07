from rest_framework import serializers
from .models import ItemPost

class ItemPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPost
        fields = "__all__"

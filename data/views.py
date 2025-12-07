from rest_framework import viewsets
from .models import ItemPost
from .serializers import ItemPostSerializer

class ItemPostViewSet(viewsets.ModelViewSet):
    queryset = ItemPost.objects.all().order_by('-created_at')
    serializer_class = ItemPostSerializer

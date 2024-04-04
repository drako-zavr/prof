from rest_framework import generics
from ...models import Memory
from ..serializers import MemorySerializer

class MemoryAPIView(generics.ListAPIView):
    """
    Memory
    """
    serializer_class = MemorySerializer
    queryset = Memory.objects.order_by("id")
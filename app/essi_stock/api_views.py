from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Categorite
from .serializers import CategorySerializer


class Stock(APIView):
    def get(self, request):
        item = Categorite.objects.all()
        serializer =CategorySerializer(item, many=True)
        return Response(serializer.data)

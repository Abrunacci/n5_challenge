from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import InfractionSerializer
# Create your views here.


class CreateInfractionView(APIView):
    def post(self, request):
        serializer = InfractionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Infraction saved."}, status=status.HTTP_200_OK)
        return Response({"message": "Unexpected esdrror"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Infraction
from .serializers import InfractionSerializer

# Create your views here.


class CreateInfractionView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = InfractionSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.validate(request.data) and serializer.is_valid(
            raise_exception=True
        ):
            serializer.save()
            return Response({"message": "Infraction saved."}, status=status.HTTP_200_OK)


class InfractionReportView(APIView):
    def get(self, request):
        email = request.data["email"]

        infractions = Infraction.objects.filter(person__email=email)

        return Response(
            InfractionSerializer(infractions, many=True).data, status=status.HTTP_200_OK
        )

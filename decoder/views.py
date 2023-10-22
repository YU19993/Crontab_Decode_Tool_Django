from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CronExpressionSerializer
from .utils import decode_crontab
from django.shortcuts import render

@api_view(['POST'])
def decode(request):
    serializer = CronExpressionSerializer(data=request.data)
    if serializer.is_valid():
        expression = serializer.validated_data['expression']
        decoded_expression = decode_crontab(expression)
        return Response({'decoded_expression': decoded_expression}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return render(request, 'index.html')
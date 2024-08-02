from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
import re

@api_view(['POST'])
def bfhl_post(request):
    data = request.data.get('data', [])
    if not isinstance(data, list):
        return Response({'is_success': False, 'message': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)

    numbers = [item for item in data if re.match(r'^\d+$', item)]
    alphabets = [item for item in data if re.match(r'^[a-zA-Z]$', item)]
    highest_alphabet = max(alphabets, key=str.upper, default="")

    user = User.objects.first()  # Assuming we use the first user for demo purposes

    response_data = {
        'is_success': True,
        'user_id': user.user_id(),
        'email': user.email,
        'roll_number': user.roll_number,
        'numbers': numbers,
        'alphabets': alphabets,
        'highest_alphabet': highest_alphabet
    }
    return Response(response_data)

@api_view(['GET'])
def bfhl_get(request):
    return Response({'operation_code': 1}, status=status.HTTP_200_OK)

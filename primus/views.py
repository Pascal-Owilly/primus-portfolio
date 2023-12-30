from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import Payment, UserPhoneNumber
from django_daraja.mpesa.core import MpesaClient
from fcm_django.models import FCMDevice
from .serializers import UserPhoneNumberSerializer
from rest_framework import status
from django.http import JsonResponse

@api_view(['POST'])
@renderer_classes([JSONRenderer])
def initiate_payment(request):
    if request.method == 'POST':
        try:
            # Check if 'amount' is present in the request data
            if 'amount' not in request.data:
                return Response({'error': 'Amount is required in the request data.'}, status=status.HTTP_400_BAD_REQUEST)

            # Validate and convert 'amount' to cents
            amount_str = request.data['amount']
            if not amount_str:
                return Response({'error': 'Amount cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)

            amount = int(round(float(amount_str) * 1))  # Convert to cents

            serializer = UserPhoneNumberSerializer(data=request.data)
            if serializer.is_valid():
                phone_number = serializer.validated_data['phone_number']
                account_reference = 'DrPrimusOchieng'
                transaction_desc = 'Description'
                callback_url = 'https://primus-ten.vercel.app/payment-status'

                try:
                    # Save the entered phone number
                    user_phone, created = UserPhoneNumber.objects.get_or_create(phone_number=phone_number)

                    # Initiate STK push
                    cl = MpesaClient()
                    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

                    # Assuming the payment is successful, send a push notification
                    if "Success" in response:
                        send_push_notification(phone_number, "Payment successful!")

                    return Response({'message': 'Payment initiated successfully'}, status=status.HTTP_200_OK)
                except Exception as e:
                    # Print the exception for debugging purposes
                    print(f"Error initiating STK push: {e}")
                    return Response({'error': 'Error initiating STK push. Check logs for details.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Handle other unexpected exceptions
            print(f"Unexpected error: {e}")
            return Response({'error': 'Unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# views.py

@api_view(['GET'])
def get_amount(request):
    try:
        # Assuming there is a fixed service amount for all customers
        fixed_amount = 3500  # Replace this with your actual fixed amount
        return Response({'amount': fixed_amount}, status=200)
    except Payment.DoesNotExist:
        return Response({'error': 'No payments found'}, status=404)
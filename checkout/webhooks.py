# myapp/views.py

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from django.conf import settings
from checkout.webhook_handler import StripeWH_Handler


# This is your test secret API key.
stripe.api_key = settings.STRIPE_SECRET_KEY

# Replace this endpoint secret with your endpoint's unique secret
endpoint_secret = settings.STRIPE_WH_SECRET


@csrf_exempt
def webhook(request):

    if request.method == 'POST':


        payload = request.body

        event = None

        try:
            event = json.loads(payload)

        except json.decoder.JSONDecodeError as e:
            print('⚠️  Webhook error while parsing basic request.' + str(e))
            return JsonResponse({'success': False})

        if endpoint_secret:
            # Only verify the event if there is an endpoint secret defined
            # Otherwise use the basic event deserialized with json
            sig_header = request.headers.get('stripe-signature')

            try:
                event = stripe.Webhook.construct_event(
                    payload, sig_header, endpoint_secret
                )

            except stripe.error.SignatureVerificationError as e:
                print('⚠️  Webhook signature verification failed.' + str(e))
                return JsonResponse({'success': False})

        # Handle the event
        # Set up a webhook handler
        handler = StripeWH_Handler(request)

        # Map webhook events to relevant handler functions
        event_map = {
            'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
            'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
        }

        # Get the webhook type from Stripe
        event_type = event['type']

        # If there's a handler for it, get it from the event map
        # Use the generic one by default
        event_handler = event_map.get(event_type, handler.handle_event)

        # Call the event handler with the event
        response = event_handler(event)
                
        return response

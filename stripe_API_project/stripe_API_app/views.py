import stripe
from django.views import View
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import Product


stripe.api_key = settings.STRIPE_SECRET_KEY
YOUR_DOMAIN = "http://127.0.0.1:8000"


class ProductLandingPageView(TemplateView):
    template_name = "landing.html"
    def get_context_data(self, **kwargs):
        product = Product.objects.get(name="Test Product")
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        checkout_session = stripe.checkout.Session.create(
            success_url=YOUR_DOMAIN + "/success/",
            cancel_url=YOUR_DOMAIN + "/cancel/",
            line_items=[
                {
                    "price": "price_H5ggYwtDq4fbrJ",
                    "quantity": 2,
                },
            ],
            mode="payment",
        )
        return JsonResponse({
            'id': checkout_session.id
        })

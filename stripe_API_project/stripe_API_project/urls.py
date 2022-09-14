from django.contrib import admin
from django.urls import path
from stripe_API_app.views import (
    CreateCheckoutSessionView,
    ProductLandingPageView
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductLandingPageView.as_view(), name='landing-page'),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view())
]

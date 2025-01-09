from django.urls import path
from products.views import ProductListView, ProductPaymentView


urlpatterns = [
    path(
        "products/",
        ProductListView.as_view(),
        name="products",
    ),
    path(
        "product-payment/",
        ProductPaymentView.as_view(),
    ),
]

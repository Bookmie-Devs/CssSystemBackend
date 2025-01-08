from rest_framework.serializers import ModelSerializer, CharField, UUIDField, Serializer
from products.models import Product


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = [
            "product_id",
            "created_at",
            "last_updated",
        ]

class ProductPaymentSerializer(Serializer):
    reference = CharField()
    transaction = CharField()
    product_id = UUIDField()

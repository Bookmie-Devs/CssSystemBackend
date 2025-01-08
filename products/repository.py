from products.models import Product, ProductPayment


class ProductRepo:
    model = Product.objects

    @classmethod
    def get_all_products(cls):
        """Fetches all products."""
        return cls.model.all()

    @classmethod
    def get_product_by_id(cls, product_id):
        """Fetches a product by its ID."""
        return cls.model.filter(pk=product_id).first()


class ProductPaymentRepository:
    model = ProductPayment.objects

    @classmethod
    def create_payment(cls, transaction, product, reference):
        payment = cls.model.create(
            transaction=transaction,
            product=product,
            reference=reference,
        )
        return payment

    # def get_payment_by_id(self, payment_id):
    #     try:
    #         return ProductPayment.objects.get(payment_id=payment_id)
    #     except ProductPayment.DoesNotExist:
    #         return None
    #

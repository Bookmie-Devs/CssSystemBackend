from products.models import Product

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






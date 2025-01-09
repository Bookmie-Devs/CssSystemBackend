from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
import json
from utils.utils import send_sms_message, normalize_phone
from products.utils import verify_payment, payment_is_confirm
from products.repository import ProductPaymentRepository, ProductRepo


def product_payment_service(request, serializer_class):
    product_repo = ProductRepo
    payment_repo = ProductPaymentRepository
    ok = HTTP_200_OK
    bad = HTTP_400_BAD_REQUEST
    json_ld = json.loads

    serializer = serializer_class(data=request.data)
    if serializer.is_valid(raise_exception=True):
        reference = serializer.validated_data.get("reference")
        transaction = serializer.validated_data.get("transaction")
        product_id = serializer.validated_data.get("product_id")
        product = product_repo.get_product_by_id(product_id=product_id)
        res = verify_payment(reference=reference)
        status, phone = payment_is_confirm(res, product.price)
        if status:
            payment = payment_repo.create_payment(
                reference=reference,
                phone=phone,
                transaction=transaction,
                product=product,
            )
            context = {
                "status": True,
                "message": "product Purchase was successfull",
            }
            send_sms_message(
                phone,
                "product_purchase.txt",
                {
                    "purchase_code": payment.transaction_validation_code,
                    "product_name": payment.product.product_name,
                },
            )
            return ok, context
        else:
            context = {
                "status": False,
                "message": "Product Purchase was unsuccessfull",
                "data": {"type": json_ld(res.content)},
            }
            # print(json_ld(res.content))
            return bad, context

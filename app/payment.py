import var_dump as var_dump
from yookassa import Payment, Configuration
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.receipt import Receipt, ReceiptItem
from yookassa.domain.common.confirmation_type import ConfirmationType
from yookassa.domain.request.payment_request_builder import PaymentRequestBuilder
import uuid

Configuration.account_id = "465315"
Configuration.secret_key = "test_TO7LIbF-V4YomTVfY7k0w8EiPqdeSUucRsI2PMjZoI4"

def pay_generation(coins: int):
    receipt = Receipt()
    receipt.customer = {"email": "test@email.com"}
    receipt.tax_system_code = 1
    receipt.items = [
        ReceiptItem({
            "description": "Коины 200",
            "quantity": coins,
            "amount": {
                "value": 1.0,
                "currency": Currency.RUB
            },
            "vat_code": 1,
            "payment_subject": "payment",
            "payment_mode": "full_payment"
        })
    ]

    builder = PaymentRequestBuilder()
    builder.set_amount({"value": coins, "currency": Currency.RUB}) \
        .set_confirmation({"type": ConfirmationType.REDIRECT, "return_url": "https://merchant-site.ru/return_url"}) \
        .set_capture(False) \
        .set_description("Заказ №72") \
        .set_metadata({"orderNumber": "72"}) \
        .set_receipt(receipt)

    request = builder.build()

    res = Payment.create(request)
    
    return res.confirmation.confirmation_url

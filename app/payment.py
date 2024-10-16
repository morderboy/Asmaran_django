from yookassa import Payment, Configuration
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.receipt import Receipt, ReceiptItem
from yookassa.domain.common.confirmation_type import ConfirmationType
from yookassa.domain.request.payment_request_builder import PaymentRequestBuilder
from yookassa.domain.common import PaymentMethodType as pay_type
import uuid

Configuration.account_id = "447171"
Configuration.secret_key = "live_auAMOrZIT8GZZI9WsqTnxetDUKNhcQiW6chNwwt-5sU"

def pay_generation(coins: int, order_id: int, email: str):
    receipt = Receipt()
    receipt.customer = {"email": email}
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
        .set_confirmation({"type": ConfirmationType.REDIRECT, "return_url": "https://asmaran.ru/payment-confirm"}) \
        .set_capture(False) \
        .set_description(f"Заказ №{order_id}") \
        .set_metadata({"orderNumber": order_id}) \
        .set_receipt(receipt)

    request = builder.build()

    res = Payment.create(request)
    
    return res.confirmation.confirmation_url, res.id, res.created_at

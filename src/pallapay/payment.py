import hashlib
from pydantic import validate_arguments
from pallapay.request import RequestsApi
from pallapay.schema import CreatePaymentRequestModel, CreatePaymentResponseModel
from pallapay.enums import *


class Payment:
    @validate_arguments
    def __init__(self, base_url: str = 'https://www.pallapay.com') -> None:
        self.consumer = RequestsApi(
            base_url=base_url,
        )

    @validate_arguments()
    def create_payment(self, merchant_id: str, order_id: str, amount: float, currency: str, payer_first_name: str,
                       payer_last_name: str, payer_email: str, custom_data=None) -> dict:
        """
        :param merchant_id: str = Your merchant ID (required)
        :param order_id: str = Order ID for your payment (required)
        :param amount: float = Amount in selected currency (required)
        :param currency: str = Currency of the payment (required)
        :param payer_first_name: str = Payer first name (required)
        :param payer_last_name: str = Payer last name (required)
        :param payer_email: str = Payer email address (required)
        :param custom_data = Custom data to get in callback (optional)
        :return: dict
        """
        params = CreatePaymentRequestModel(merchant=merchant_id, order=order_id, amount=amount, currency=currency,
                                           first_name=payer_first_name, last_name=payer_last_name, email=payer_email,
                                           custom=custom_data).dict(exclude_none=True)
        response = self.consumer.post('/api/v1/request/createOrder', json=params)
        return CreatePaymentResponseModel(**response.json()['result']).dict()

    @validate_arguments
    def is_transaction_paid(self, merchant_password: str, hash_string: str, total: str, date: str, id_transfer: str, status: str) -> bool:
        """
        :param merchant_password: str = Your merchant password (required)
        :param hash_string: str = IPN request hash that pallapay sent to your IPN_NOTIFY page (required)
        :param total: str = IPN request total that pallapay sent to your IPN_NOTIFY page (required)
        :param date: str = IPN request date that pallapay sent to your IPN_NOTIFY page (required)
        :param id_transfer: str = IPN request id_transfer that pallapay sent to your IPN_NOTIFY page (required)
        :param id_transfer: str = IPN request id_transfer that pallapay sent to your IPN_NOTIFY page (required)
        :param status: str = IPN request status that pallapay sent to your IPN_NOTIFY page (required)
        :return: bool
        """
        if status.upper() != CONFIRMED_STATUS:
            return False

        request_hash = hashlib.md5(f"{total}:{merchant_password}:{date}:{id_transfer}".encode('utf-8')).hexdigest().upper()
        return hash_string == request_hash

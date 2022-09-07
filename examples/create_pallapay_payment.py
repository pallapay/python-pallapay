from pallapay.payment import Payment
from pallapay.enums import *


def create_payment():
    # AVAILABLE CURRENCY CONSTANTS :
    # -> CURRENCY_AED
    # -> CURRENCY_USD
    # -> CURRENCY_EUR
    # -> CURRENCY_GBP
    # -> CURRENCY_BTC
    # -> CURRENCY_ETH
    # -> CURRENCY_TRX
    # -> CURRENCY_PALLA_TRC20
    # -> CURRENCY_USDT_TRC20
    # -> CURRENCY_USDT_ERC20
    # -> CURRENCY_USDC_ERC20
    # -> CURRENCY_DAI_ERC20

    # Create payment link
    payment = Payment()
    result = payment.create_payment('YOUR_MERCHANT_ID', 'YOUR_ORDER_ID', 100, CURRENCY_AED, 'PAYER_FIRST_NAME',
                                    'PAYER_LAST_NAME', 'payer@mail.com', 'YOUR_CUSTOM_DATA')

    print(result['redirect_to_url'])


def ipn_handler():
    # TODO : Get all form data
    form_data = {
        'hash': 'B6428DAC2C62427CB3A59A4203B88AD8',
        'total': '100',
        'date': 'RECEIVED_DATE',
        'id_transfer': 'RECEIVED_ID_TRANSFER',
        'status': 'CONFIRMED',
    }

    payment = Payment()
    is_paid = payment.is_transaction_paid('YOUR_MERCHANT_PASSWORD', form_data['hash'], form_data['total'],
                                          form_data['date'], form_data['id_transfer'], form_data['status'])
    if is_paid:
        print('CONFIRMED PAYMENT')
    else:
        print('NOT PAID')


if __name__ == '__main__':
    create_payment()

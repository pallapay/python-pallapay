## Pallapay crypto payment gateway SDK

Easy to use SDK for pallapay crypto payment gateway, accept crypto in your website and get paid in cash.


#### Installation
```
pip install python-pallapay
```

#### Easy to use

First signup and [get you merchant ID from pallapay website](https://www.pallapay.com/account/merchants/add)

Then you can create a payment link:

```python
from pallapay.payment import Payment
from pallapay.enums import *

def create_payment():
    # Create payment link
    
    payment = Payment()
    result = payment.create_payment(merchant_id='YOUR_MERCHANT_ID', order_id='YOUR_ORDER_ID', amount=100,
                                    currency=CURRENCY_AED, payer_first_name='PAYER_FIRST_NAME',
                                    payer_last_name='PAYER_LAST_NAME', payer_email='payer@mail.com',
                                    custom_data='YOUR_CUSTOM_DATA')

    print(result['redirect_to_url'])
```

`create_payment` params:

| Name             | Description                                                                                                        | Required |
|------------------|--------------------------------------------------------------------------------------------------------------------|----------|
| merchant_id      | Your merchant ID (You can create one in pallapay panel)                                                            | YES      |
| order_id         | Order ID for your payment                                                                                          | YES      |
| amount           | Amount in selected currency                                                                                        | YES      |
| currency         | Currency of the payment (You can find all available currencies down bellow)                                        | YES      |
| payer_first_name | Payer first name                                                                                                   | YES      |
| payer_last_name  | Payer last name                                                                                                    | YES      |
| payer_email      | Payer email                                                                                                        | YES      |
| custom_data      | You can pass your custom data here. for example, your customers order ID. This item is not displayed to the buyer. | NO       |


After that you can redirect user to `redirect_to_url`.

#### Handle IPN

After user payment was done, we will call your IPN_NOTIFY_URL that you entered when you created your merchant.

In that page you can use this `is_transaction_paid` method to check if payment was valid and paid.

```python
from pallapay.payment import Payment

def ipn_handler():
    # Checking IPN_NOTIFY request that pallapay will send to your IPN_NOTIFY_URL

    # TODO : Get all form data
    form_data = {
        'hash': 'B6428DAC2C62427CB3A59A4203B88AD8',
        'total': '100',
        'date': 'RECEIVED_DATE',
        'id_transfer': 'RECEIVED_ID_TRANSFER',
        'status': 'CONFIRMED',
    }

    payment = Payment()
    is_paid = payment.is_transaction_paid(merchant_password='YOUR_MERCHANT_PASSWORD', hash_string=form_data['hash'],
                                          total=form_data['total'], date=form_data['date'],
                                          id_transfer=form_data['id_transfer'], status=form_data['status'])
    if is_paid:
        print('CONFIRMED PAYMENT')
    else:
        print('NOT PAID')
```

Received data on your IPN_NOTIFY:

| name          | Description                                                                                                                      |
|---------------|----------------------------------------------------------------------------------------------------------------------------------|
| amount        | The received amount without commissions                                                                                          |
| fee           | Fee that was paid (Note: Paid by the buyer or merchant according to the merchant settings in pallapay dashboard)                 |
| total         | Total transaction amount including commission                                                                                    |
| currency      | Transaction currency                                                                                                             |
| payer         | Payer name                                                                                                                       |
| receiver      | Merchant username in Pallapay                                                                                                    |
| status        | Transaction status                                                                                                               |
| date          | Transaction date                                                                                                                 |
| id_transfer   | Unique transaction number in Pallapay                                                                                            |
| merchant_name | Merchant name                                                                                                                    |
| merchant_id   | Merchant ID                                                                                                                      |
| balance       | Available merchant balance in transaction currency                                                                               |
| item_name     | Item name                                                                                                                        |
| custom        | Custom data that you sent for create payment                                                                                     |
| hash          | encrypted hash to check validity of IPN request (Note: You can check by yourself or you can check by is_transaction_paid method) |

#### Supported currencies

| Supported Currencies |
|----------------------|
| AED                  |
| USD                  |
| EUR                  |
| GBP                  |
| BTC                  |
| ETH                  |
| TRON                 |
| PALLA                |
| USDT-TRC20           |
| USDT-ERC20           |
| USDC-ERC20           |
| DAI-ERC20            |

And you can find supported currencies constants here:

```python
from pallapay.enums import *

CURRENCY_AED
CURRENCY_USD
CURRENCY_EUR
CURRENCY_GBP
CURRENCY_BTC
CURRENCY_ETH
CURRENCY_TRX
CURRENCY_PALLA_TRC20
CURRENCY_USDT_TRC20
CURRENCY_USDT_ERC20
CURRENCY_USDC_ERC20
CURRENCY_DAI_ERC20
```

#### Contribution

Contributions are highly appreciated either in the form of pull requests for new features, bug fixes or just bug reports.

----------------------------------------------

[Pallapay Website](https://www.pallapay.com)

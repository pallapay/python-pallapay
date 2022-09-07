import os
import pytest
from pallapay.payment import Payment


def init_payment_with_base_url():
    Payment(base_url='https://www.pallapay.com')
    print('Pallapay test payment client created successfully.')


def test_init_payment_with_wrong_base_url():
    with pytest.raises(Exception) as e:
        print(e)
        Payment(base_url=12345)

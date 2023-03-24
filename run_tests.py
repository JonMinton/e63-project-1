import unittest

# Add specific testclasses here
from tests.customer_test import TestCustomer
from tests.bank_test import TestBank
from tests.account_test import TestAccount
from tests.merchant_test import TestMerchant
from tests.transaction_test import TestTransaction
from tests.tag_test import TestTag

if __name__ == "__main__":
    unittest.main()
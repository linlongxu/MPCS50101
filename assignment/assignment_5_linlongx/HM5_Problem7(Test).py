import unittest

class TestEmailValidation(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(validate_email("johndoe@domainsample.com"))
        self.assertTrue(validate_email("john.doe+spamfilter@domainsample.co.uk"))

    def test_invalid_emails(self):
        self.assertFalse(validate_email("@domainsample.com"))
        self.assertFalse(validate_email("johndoedomainsample.com"))

if __name__ == "__main__":
    unittest.main()
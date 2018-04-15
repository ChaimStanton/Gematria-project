from unittest import TestCase


class TestCalculateGamatria(TestCase):
    def test_calculate_gematria(self):
        from miscellaneous_functions import calculate_gematria
        self.assertEqual(int(calculate_gematria("ובני פלוא אליאב")), int(299))

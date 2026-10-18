import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import checkout as subject


class IndependentAcceptance(unittest.TestCase):
    def purchase(self, **values):
        return {"id": 'customer"\n42', "items": [
            {"price": 25, "quantity": 2},
            {"price": 50, "quantity": 1}], **values}

    def test_real_receipt_and_results_for_promotion_variants(self):
        for extra, total in [({}, 100), ({"promotion": "SAVE10"}, 90),
                             ({"promotion": "UNKNOWN"}, 100)]:
            with self.subTest(extra=extra), tempfile.TemporaryDirectory() as d:
                order = self.purchase(**extra)
                original = copy.deepcopy(order)
                path = Path(d) / "receipt.json"
                result = subject.checkout(order, path)
                self.assertEqual(result, {"total": total, "payment": "paid"})
                self.assertEqual(json.loads(path.read_text(encoding="utf-8")),
                                 {"order_id": order["id"], "total": total})
                self.assertEqual(order, original)

    def test_gateway_reads_already_written_receipt(self):
        for decline in [False, True]:
            with self.subTest(decline=decline), tempfile.TemporaryDirectory() as d:
                path = Path(d) / "receipt.json"
                order = self.purchase(promotion="SAVE10", decline=decline)
                gateway = subject.charge
                observed = []

                def observe(purchase, total):
                    observed.append(json.loads(path.read_text(encoding="utf-8")))
                    self.assertIs(purchase, order)
                    self.assertEqual(total, 90)
                    return gateway(purchase, total)

                with patch.object(subject, "charge", side_effect=observe):
                    if decline:
                        with self.assertRaisesRegex(ValueError, "^payment declined$"):
                            subject.checkout(order, path)
                    else:
                        self.assertEqual(subject.checkout(order, path),
                                         {"total": 90, "payment": "paid"})
                expected = {"order_id": order["id"], "total": 90}
                self.assertEqual(observed, [expected])
                self.assertEqual(json.loads(path.read_text(encoding="utf-8")), expected)

    def test_empty_order_never_writes_or_pays(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "receipt.json"
            with patch.object(subject, "charge") as charge:
                with self.assertRaisesRegex(ValueError, "^empty order$"):
                    subject.checkout(self.purchase(items=[]), path)
            self.assertFalse(path.exists())
            charge.assert_not_called()

    def test_real_filesystem_failure_prevents_gateway(self):
        with tempfile.TemporaryDirectory() as d:
            with patch.object(subject, "charge") as charge:
                with self.assertRaises(IsADirectoryError):
                    subject.checkout(self.purchase(), Path(d))
            charge.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)

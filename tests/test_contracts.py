import unittest

import torch

from tfm_pytorch_book.contracts import TensorContract, validate_context_query


class TensorContractTests(unittest.TestCase):
    def test_tensor_contract_reports_semantic_axes(self) -> None:
        contract = TensorContract(("batch", "rows", "columns"))

        with self.assertRaisesRegex(ValueError, "batch, rows, columns"):
            contract.validate(torch.zeros(2, 3), name="x")

    def test_context_query_contract_rejects_mismatched_targets(self) -> None:
        x = torch.zeros(2, 5, 3)
        y_context = torch.zeros(2, 2, dtype=torch.long)

        with self.assertRaisesRegex(ValueError, "batch, n_context"):
            validate_context_query(x, y_context, n_context=3)

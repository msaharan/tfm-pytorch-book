import unittest

import torch

from tfm_pytorch_book import MiniTFM


def make_model() -> MiniTFM:
    torch.manual_seed(7)
    model = MiniTFM(n_columns=3, embed_dim=8, n_classes=2)
    model.eval()
    return model


class MiniTFMTests(unittest.TestCase):
    def test_output_shape_contains_query_rows_only(self) -> None:
        model = make_model()
        x = torch.randn(2, 6, 3)
        y_context = torch.tensor([[0, 1, 0, 1], [1, 0, 1, 0]])

        logits = model(x, y_context, n_context=4)

        self.assertEqual(logits.shape, (2, 2, 2))

    def test_one_query_row_cannot_influence_another(self) -> None:
        model = make_model()
        x = torch.randn(1, 6, 3)
        y_context = torch.tensor([[0, 1, 0, 1]])
        changed = x.clone()
        changed[:, 4] += 100

        original_logits = model(x, y_context, n_context=4)
        changed_logits = model(changed, y_context, n_context=4)

        torch.testing.assert_close(original_logits[:, 1], changed_logits[:, 1])
        self.assertFalse(torch.allclose(original_logits[:, 0], changed_logits[:, 0]))

    def test_context_labels_can_influence_predictions(self) -> None:
        model = make_model()
        x = torch.randn(1, 6, 3)
        labels_a = torch.tensor([[0, 0, 0, 0]])
        labels_b = torch.tensor([[1, 1, 1, 1]])

        logits_a = model(x, labels_a, n_context=4)
        logits_b = model(x, labels_b, n_context=4)

        self.assertFalse(torch.allclose(logits_a, logits_b))

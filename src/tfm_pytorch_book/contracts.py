"""Small helpers for making tensor contracts executable."""

from dataclasses import dataclass

import torch


@dataclass(frozen=True)
class TensorContract:
    """Describe and validate the semantic axes of a tensor."""

    axes: tuple[str, ...]

    def validate(self, tensor: torch.Tensor, *, name: str = "tensor") -> None:
        if tensor.ndim != len(self.axes):
            expected = ", ".join(self.axes)
            raise ValueError(
                f"{name} must have {len(self.axes)} axes ({expected}); "
                f"received shape {tuple(tensor.shape)}"
            )


TABLE = TensorContract(("batch", "rows", "columns"))
CONTEXT_TARGETS = TensorContract(("batch", "context_rows"))


def validate_context_query(
    x: torch.Tensor, y_context: torch.Tensor, n_context: int
) -> None:
    """Validate the public context/query contract used by ``MiniTFM``."""

    TABLE.validate(x, name="x")
    CONTEXT_TARGETS.validate(y_context, name="y_context")

    if not 0 < n_context < x.shape[1]:
        raise ValueError("n_context must leave at least one context and query row")
    if y_context.shape != (x.shape[0], n_context):
        raise ValueError(
            "y_context must have shape (batch, n_context); "
            f"received {tuple(y_context.shape)}"
        )


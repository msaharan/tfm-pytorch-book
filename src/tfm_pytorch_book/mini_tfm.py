"""A deliberately small in-context predictor used throughout the book."""

import torch
from torch import nn

from tfm_pytorch_book.contracts import validate_context_query


class MiniTFM(nn.Module):
    """Predict query labels from table values and labeled context rows.

    This is an educational model, not a competitive pretrained TFM. Its public
    contract makes the context/query information boundary explicit.
    """

    def __init__(
        self,
        n_columns: int,
        embed_dim: int,
        n_classes: int,
        n_heads: int = 2,
    ) -> None:
        super().__init__()
        if embed_dim % n_heads != 0:
            raise ValueError("embed_dim must be divisible by n_heads")

        self.n_columns = n_columns
        self.value_projection = nn.Linear(1, embed_dim)
        self.column_embedding = nn.Parameter(
            torch.randn(1, 1, n_columns, embed_dim) * 0.02
        )
        self.target_embedding = nn.Embedding(n_classes, embed_dim)
        self.context_attention = nn.MultiheadAttention(
            embed_dim, n_heads, batch_first=True
        )
        self.output_norm = nn.LayerNorm(embed_dim)
        self.output_head = nn.Linear(embed_dim, n_classes)

    def forward(
        self, x: torch.Tensor, y_context: torch.Tensor, n_context: int
    ) -> torch.Tensor:
        validate_context_query(x, y_context, n_context)
        if x.shape[2] != self.n_columns:
            raise ValueError(
                f"x must have {self.n_columns} columns; received {x.shape[2]}"
            )

        cell_states = self.value_projection(x.unsqueeze(-1))
        cell_states = cell_states + self.column_embedding
        row_states = cell_states.mean(dim=2)

        context_states = row_states[:, :n_context]
        context_states = context_states + self.target_embedding(y_context)
        query_states = row_states[:, n_context:]

        query_updates, _ = self.context_attention(
            query=query_states,
            key=context_states,
            value=context_states,
            need_weights=False,
        )
        return self.output_head(self.output_norm(query_states + query_updates))


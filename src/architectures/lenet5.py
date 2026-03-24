import torch
import torch.nn as nn


class LeNet5(nn.Module):
    """
    LeCun et al., 1998 — Gradient-Based Learning Applied to Document Recognition.

    Original used tanh + average pooling; this version uses ReLU + max pooling
    which is the common modern variant.

    Args:
        num_classes: number of output classes (default 10 for MNIST)
        in_channels: input channels (1 for grayscale, 3 for RGB)
    """

    def __init__(self, num_classes: int = 10, in_channels: int = 1):
        super().__init__()
        # TODO: implement

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # TODO: implement
        raise NotImplementedError

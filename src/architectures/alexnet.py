import torch
import torch.nn as nn


class AlexNet(nn.Module):
    """
    Krizhevsky, Sutskever, Hinton, 2012 — ImageNet Classification with Deep CNNs.

    Adapted for variable input size (original: 224×224).

    Args:
        num_classes: number of output classes (default 1000 for ImageNet)
        dropout: dropout probability in the classifier head
    """

    def __init__(self, num_classes: int = 1000, dropout: float = 0.5):
        super().__init__()
        # TODO: implement

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # TODO: implement
        raise NotImplementedError

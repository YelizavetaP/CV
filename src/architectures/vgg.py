import torch
import torch.nn as nn


# Conv layer counts per block for VGG-11/13/16/19
CONFIGS = {
    "vgg11": [1, 1, 2, 2, 2],
    "vgg13": [2, 2, 2, 2, 2],
    "vgg16": [2, 2, 3, 3, 3],
    "vgg19": [2, 2, 4, 4, 4],
}


class VGG(nn.Module):
    """
    Simonyan & Zisserman, 2014 — Very Deep Convolutional Networks.

    Args:
        variant: one of 'vgg11', 'vgg13', 'vgg16', 'vgg19'
        num_classes: number of output classes
        dropout: dropout probability in classifier
    """

    def __init__(
        self,
        variant: str = "vgg16",
        num_classes: int = 1000,
        dropout: float = 0.5,
    ):
        super().__init__()
        assert variant in CONFIGS, f"Unknown variant '{variant}'"
        # TODO: implement

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # TODO: implement
        raise NotImplementedError

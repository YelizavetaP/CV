import torch
import torch.nn as nn


class DepthwiseSeparableConv(nn.Module):
    """Depthwise conv (per-channel 3×3) followed by pointwise conv (1×1)."""

    def __init__(self, in_channels: int, out_channels: int, stride: int = 1):
        super().__init__()
        # TODO: implement

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # TODO: implement
        raise NotImplementedError


class InvertedResidual(nn.Module):
    """MobileNetV2 inverted residual block (expand → depthwise → project)."""

    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        stride: int = 1,
        expand_ratio: int = 6,
    ):
        super().__init__()
        # TODO: implement

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # TODO: implement
        raise NotImplementedError


class MobileNetV1(nn.Module):
    """
    Howard et al., 2017 — MobileNets: Efficient CNNs for Mobile Vision Applications.

    Args:
        num_classes: number of output classes
        width_multiplier: scales number of channels (alpha in paper)
    """

    def __init__(self, num_classes: int = 1000, width_multiplier: float = 1.0):
        super().__init__()
        # TODO: implement

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # TODO: implement
        raise NotImplementedError


class MobileNetV2(nn.Module):
    """
    Sandler et al., 2018 — MobileNetV2: Inverted Residuals and Linear Bottlenecks.

    Args:
        num_classes: number of output classes
        width_multiplier: scales number of channels
    """

    def __init__(self, num_classes: int = 1000, width_multiplier: float = 1.0):
        super().__init__()
        # TODO: implement

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # TODO: implement
        raise NotImplementedError

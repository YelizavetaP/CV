import torch
import torch.nn as nn


class BasicBlock(nn.Module):
    """Residual block for ResNet-18 / 34 (no bottleneck)."""

    expansion = 1

    def __init__(self, in_channels: int, out_channels: int, stride: int = 1):
        super().__init__()
        # TODO: implement

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # TODO: implement
        raise NotImplementedError


class Bottleneck(nn.Module):
    """Bottleneck residual block for ResNet-50 / 101 / 152."""

    expansion = 4

    def __init__(self, in_channels: int, out_channels: int, stride: int = 1):
        super().__init__()
        # TODO: implement

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # TODO: implement
        raise NotImplementedError


class ResNet(nn.Module):
    """
    He et al., 2015 — Deep Residual Learning for Image Recognition.

    Args:
        block: BasicBlock (ResNet-18/34) or Bottleneck (ResNet-50/101/152)
        layers: number of blocks per stage, e.g. [2, 2, 2, 2] for ResNet-18
        num_classes: number of output classes
    """

    def __init__(
        self,
        block: type,
        layers: list[int],
        num_classes: int = 1000,
    ):
        super().__init__()
        # TODO: implement

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # TODO: implement
        raise NotImplementedError


def resnet18(num_classes: int = 1000) -> ResNet:
    return ResNet(BasicBlock, [2, 2, 2, 2], num_classes)


def resnet34(num_classes: int = 1000) -> ResNet:
    return ResNet(BasicBlock, [3, 4, 6, 3], num_classes)


def resnet50(num_classes: int = 1000) -> ResNet:
    return ResNet(Bottleneck, [3, 4, 6, 3], num_classes)


def resnet101(num_classes: int = 1000) -> ResNet:
    return ResNet(Bottleneck, [3, 4, 23, 3], num_classes)

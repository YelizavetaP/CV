"""Generic training loop reusable across all architectures."""
import torch
import torch.nn as nn
from torch.utils.data import DataLoader


def train_one_epoch(
    model: nn.Module,
    loader: DataLoader,
    optimizer: torch.optim.Optimizer,
    criterion: nn.Module,
    device: torch.device,
) -> dict:
    """Returns dict with 'loss' and 'acc' for the epoch."""
    # TODO: implement
    raise NotImplementedError


def evaluate(
    model: nn.Module,
    loader: DataLoader,
    criterion: nn.Module,
    device: torch.device,
) -> dict:
    """Returns dict with 'loss' and 'acc'."""
    # TODO: implement
    raise NotImplementedError

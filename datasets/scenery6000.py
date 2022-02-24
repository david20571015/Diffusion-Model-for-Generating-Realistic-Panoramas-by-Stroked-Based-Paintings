import os
import glob
from turtle import right
import torchvision
import torch

from .vision import VisionDataset
from .utils import download_file_from_google_drive, check_integrity


class Scenery6000(VisionDataset):
    """
    Args:
        root (string): Root directory where images are downloaded to.
        transform (callable, optional): A function/transform that  takes in an PIL image
            and returns a transformed version. E.g, ``transforms.ToTensor``
    """

    def __init__(self, root, transform=None):
        super(Scenery6000, self).__init__(root, transform=transform)

        self.db = torchvision.datasets.ImageFolder(root=root,
                                                   transform=transform)

    def __getitem__(self, index):
        """
        Args:
            index (int): Index

        Returns:
            tuple: (image, target) where target is index of the target class.
        """
        return self.db[index]

    def __len__(self):
        return len(self.db)

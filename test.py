import torch
import torchvision.transforms as transforms
from torchvision.utils import save_image

from datasets.scenery6000 import Scenery6000

ds = Scenery6000(
    "~/../../data/dd/scenery6000/scenery",
    transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(256),
        transforms.ToTensor()
    ]))
print(ds[0][0].shape)
save_image(ds[0][0], "test.jpg")

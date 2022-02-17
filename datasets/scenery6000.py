# import os
# import glob
# import torchvision

# from PIL import Image
# from .vision import VisionDataset
# from .utils import download_file_from_google_drive, check_integrity

# class Scenery6000(VisionDataset):
#     base_folder = "scenery6000"

#     """
#     Args:
#         root (string): Root directory where images are downloaded to.
#         transform (callable, optional): A function/transform that  takes in an PIL image
#             and returns a transformed version. E.g, ``transforms.ToTensor``
#         target_transform (callable, optional): A function/transform that takes in the
#             target and transforms it.
#     """
#     def __init__(self, root, 
#                 transform=None,
#                 target_transform=None):
#         super(Scenery6000, self).__init__(root, transform=transform, target_transform=target_transform)

#         self.transform = transform
#         self.target_transform = target_transform
#         data = torchvision.datasets.ImageFolder(root=root, transform=self.transform)
        
#     def __getitem__(self, index):
#         """
#         Args:
#             index (int): Index

#         Returns:
#             tuple: (image, target) where target is index of the target class.
#         """

#         img = Image.open(os.path.join(self.root, self.base_folder, "all", self.target[index]))

#         if self.transform is not None:
#             img = self.transform(img)

#         if self.target_transform is not None:
#             target = self.target_transform(target)

#         return img, target

#     def __len__(self):
#         return len(self.data)
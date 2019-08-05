try:
    from PIL import Image
    import numpy as np
except (ModuleNotFoundError, ImportError) as e:
    e.message = ("This plugin you requested has few unmet dependencies. "
                 "Install those before continue")
    raise

from . import ImportExportBase


class ImagePlugin(ImportExportBase):
    def __init__(self, files):
        super(ImagePlugin, self).__init__()
        self.files = files

    @staticmethod
    def pil_loader(path):
        with open(path, 'rb') as f:
            img = Image.open(f)
            return img.convert('RGB')

    def load(self, file):
        # TODO: maybe use accimage in the future
        return np.array(self.pil_loader(file))

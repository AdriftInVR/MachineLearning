import os
from PIL import Image

# Paths
src_smg = r'raw/SMG'
src_smo = r'raw/SMO'

dest_smg = "train/SMG"
dest_smo = "train/SMO"

for root, dirs, files in os.walk(src_smg):
    for file in files:
        if file.lower().endswith(".jpg") or file.lower().endswith(".png") or file.lower().endswith(".jpeg"):
            foo = Image.open(os.path.join(root,file))
            foo = foo.resize((255,255),Image.ANTIALIAS)
            foo.save(os.path.join(dest_smg,file), optimize=True, quality=90)


for root, dirs, files in os.walk(src_smo):
    for file in files:
        if file.lower().endswith(".jpg") or file.lower().endswith(".png") or file.lower().endswith(".jpeg"):
            foo = Image.open(os.path.join(root,file))
            foo = foo.resize((255,255),Image.ANTIALIAS)
            foo.save(os.path.join(dest_smo,file), optimize=True, quality=90)

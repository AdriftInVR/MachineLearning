import os
import random
import shutil

# Paths
src_smg = r'train/SMG'
src_smo = r'train/SMO'

des_smg = r'test/SMG'
des_smo = r'test/SMO'

# All images

imgs_smg = []
imgs_smo = []

for root, dirs, files in os.walk(src_smg):
    for file in files:
        if file.lower().endswith(".jpg") or file.lower().endswith(".png") or file.lower().endswith(".gif") or file.lower().endswith(".jpeg"):
            imgs_smg.append(os.path.join(root,file))

for root, dirs, files in os.walk(src_smo):
    for file in files:
        if file.lower().endswith(".jpg") or file.lower().endswith(".png") or file.lower().endswith(".gif") or file.lower().endswith(".jpeg"):
            imgs_smo.append(os.path.join(root,file))

count_smg = len(imgs_smg)
count_smo = len(imgs_smo)

print(count_smg)
print(count_smo)

selection_smg = random.sample(imgs_smg, int(count_smg/5))
selection_smo = random.sample(imgs_smo, int(count_smo/5))

for img in selection_smg:
    shutil.move(img, des_smg)

for img in selection_smo:
    shutil.move(img, des_smo)
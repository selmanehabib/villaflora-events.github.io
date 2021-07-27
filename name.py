
import os
path = '/Users/selmanehabib/Desktop/Lightroom Export/Neuer Ordner/Lightroom Export'
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))
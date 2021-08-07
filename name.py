
import os
path = '/Users/selmanehabib/Desktop/30 juli 2021/Lightroom Export'
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))
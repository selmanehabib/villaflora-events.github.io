
import os
path = '/Users/selmanehabib/Documents/GitHub/villaflora-events.github.io/images/event2'
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))
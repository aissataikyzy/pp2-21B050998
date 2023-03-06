import os
path_dir = '/Users/User/Documents/pp2/.vs/pp2/TSIS6/dir file'
if os.path.exists(path_dir):
    print("Yes")
    os.remove(path_dir)
else:
    print("No")
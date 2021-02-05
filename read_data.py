import os
from path import Path

source = '/Users/sena/Desktop/project/faces'
destination = 'D:/faces'

s = Path(source)
d = Path(destination)


def transfer():
    print("Files are copied from %s to %s file." % (s, d))
    files_counter = 0
    for i in s.walk():
        if i.isfile() and i.endswith("jpg"):
            files_counter += 1
            print("Copying... %s" % i)
            i.copy(d)

    if files_counter == 0:
        print("Files not found")
    else:
        print(" %s files copied " % files_counter)


if __name__ == "__main__":
    if os.path.exists(source):
        transfer()
    else:
        print("The file path was not found.")

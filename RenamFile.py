import os

files=os.listdir('/Users/snehabhi/Downloads/prank/')
os.chdir('/Users/snehabhi/Downloads/prank/')
for fname in files:
    if fname[0] != '.':
       map=str.maketrans('','','0123456789')
       os.rename(fname,fname.translate(map))
       print("Old Name " + fname)
       print("New Name " + fname.translate(map))

print("All files are now renamed")

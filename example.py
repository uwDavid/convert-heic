import os, sys
from pillow_heif import register_heif_opener
from pathlib import Path
from PIL import Image

register_heif_opener()

directory = "C:\\Path\\to\\directory"

#print(os.listdir(directory))
#files = [f for f in os.listdir(directory) if f.endswith('.heic') or f.endswith('.heif')]

files = [os.listdir(directory)][0]
#print(files)
#print(type(files))

for filename in files:
    # print(os.path.join(directory, filename))
    image = Image.open(os.path.join(directory, filename))
    image.convert('RGB').save(os.path.join(directory, os.path.splitext(filename)[0] + '.jpg'))

""""
Example for converting heic to jpeg

# Open HEIF or HEIC file
heif_file = pyheif.read("example.heic")

# Extract the image data
image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data)

# Save as JPEG
image.save('example.jpg')


# for infile in sys.argv[1:]:
for infile in location:
    #print(infile)
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert", infile)
"""
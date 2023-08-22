# Convert HEIC-to-jpeg using Python

A Python code that can be used anywhere to convert HEIC files to any other format supported by Pillow. 

```
import os, sys
from pillow_heif import register_heif_opener
from pathlib import Path
from PIL import Image

register_heif_opener()

directory = "C:\\Path\\to\\directory"

files = [os.listdir(directory)][0]

for filename in files:
    image = Image.open(os.path.join(directory, filename))
    image.convert('RGB').save(os.path.join(directory, os.path.splitext(filename)[0] + '.jpg'))
```

## References
[Safan's Blog](https://safjan.com/convert-heic-and-heif-to-jpg-png-bmp-with-python/#:~:text=Use%20Pillow,-Step%201%3A%20Installing&text=We%20then%20use%20the%20open,image%20as%20a%20JPEG%20file) - It's a good starting point, but we couldn't use `Image.open()`

To open `HEIC` files using Pillow, there is a wonderful plug-in: 
[pillow_heif](https://github.com/bigcat88/pillow_heif)




from datetime import datetime
import pathlib
import urllib.parse

import astropy
import astropy.utils.data
import asdf
import numpy as np
import PIL
import matplotlib.pyplot as plt
import matplotlib.colors

base_url = 'https://optics.gi.alaska.edu/amisr_archive/PKR/DASC/'
wavelength = 558
time = datetime(2025, 2, 17, 10, 59, 17)

file_name = f'PFRR_{time.year:04d}{time.month:02d}{time.day:02d}_{time.hour:02d}{time.minute:02d}{time.second:02d}_{wavelength:04d}.png'
download_url = urllib.parse.urljoin(
    base_url,
    f'PNG/'
    f'{time.year:04d}/'
    f'{time.year:04d}{time.month:02d}{time.day:02d}/'
    f'{time.hour:02d}/'
    f'{file_name}',
)
image_path = astropy.utils.data.download_file(
    download_url,
    show_progress=True,
    allow_insecure=True,
    )
img = PIL.Image.open(image_path)
img_array = np.array(img)
lower, upper = np.quantile(img_array, (0.25, 0.98))
color_norm = matplotlib.colors.LogNorm(vmin=lower, vmax=np.min([upper, lower * 10]))
plt.imshow(img_array, norm=color_norm, cmap='gray', origin='lower')
plt.tight_layout()
plt.show()

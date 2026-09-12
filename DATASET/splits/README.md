# Image-level splits

These lists define the fixed image-level split for this MAD release:

| File | Images |
| --- | ---: |
| `train_images.txt` | 73,581 |
| `val_images.txt` | 16,896 |
| `test_images.txt` | 25,622 |
| Total | 116,099 |

Each line is an image file path relative to the dataset root, including the `image/` prefix. For example, `image/ATM/n02977058_5603.JPEG` identifies an image whose annotation is `label/ATM/n02977058_5603.JPEG.json`.

Some directory names contain spaces. Read the entire line as a path; do not split it on whitespace.

Every image file path appears in exactly one list. This defines non-overlap by file path, without asserting that image contents have been deduplicated.

The composition-level lists are provided separately in `../generalized-split/`. They describe the composition categories included in each split. Use the image-level lists here to determine the split of each individual image.

The lists preserve the established split assignments. Loading this release does not require rerunning a random split procedure or downloading a `.t7` file.

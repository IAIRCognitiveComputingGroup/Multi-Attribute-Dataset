# Multi-Attribute Dataset (MAD)

## Repository roles

This GitHub repository contains the MAD documentation, licensing information, split definitions, and evaluation utility. The complete downloadable dataset is hosted on Hugging Face:

**[IAIRCognitiveComputingGroup/Multi-Attribute-Dataset on Hugging Face](https://huggingface.co/datasets/IAIRCognitiveComputingGroup/Multi-Attribute-Dataset)**

The Hugging Face repository is private during release preparation. Authorized users must authenticate before downloading. The URL and commands will remain unchanged after the dataset is made public; authentication will then be optional.

## Download

Install the Hugging Face Hub CLI:

```bash
pip install --upgrade huggingface_hub
```

For private access, authenticate once:

```bash
hf auth login
```

Download the complete dataset:

```bash
hf download IAIRCognitiveComputingGroup/Multi-Attribute-Dataset \
  --repo-type dataset \
  --local-dir ./MAD-download
```

Extract the image shards and annotations:

```bash
mkdir -p ./MAD
for archive in ./MAD-download/data/images/*.tar; do
  tar -xf "$archive" -C ./MAD
done
tar -xzf ./MAD-download/data/annotations/mad-labels.tar.gz -C ./MAD
cp -r ./MAD-download/generalized-split ./MAD/
cp -r ./MAD-download/splits ./MAD/
```

After extraction, images are stored under `MAD/image/` and annotations under `MAD/label/`. Each image `image/<object>/img.JPEG` corresponds to `label/<object>/img.JPEG.json`.

## Release contents

The Hugging Face release contains:

- 116,099 source images in 14 TAR shards: 73,581 training, 16,896 validation, and 25,622 test images.
- 116,099 MAD JSON annotation files in `data/annotations/mad-labels.tar.gz`.
- Composition definitions in `generalized-split/`.
- Fixed image-level assignments in `splits/`.

The fixed release uses non-overlapping image assignments for training, validation, and testing. The 59 groups of byte-identical images found across split assignments are retained as intentionally introduced label noise, following the dataset definition.

Pretrained word-vector binaries, `.t7` files, extracted model features, and the original RAR volumes are not included.

## Evaluation utility

The repository-root [`utils.py`](../utils.py) contains `multi_evaluation`, the MAD authors' function for the proposed hard and soft multi-attribute metrics combined with object correctness. This software file is governed by the repository's BSD 3-Clause license.

## License

- Our original contributions to MAD, including the annotations and split definitions, are released under the [Creative Commons Attribution 4.0 International license (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). This permits commercial and non-commercial use, sharing, and adaptation under the license terms.
- This license covers only rights in the original MAD contributions that we are authorized to grant. It does not cover the source images, third-party pretrained embeddings, or software.
- The source images were obtained through ImageNet, and their copyrights remain with their respective rights holders. Users must comply with the applicable image rights and access conditions; the MAD annotation license grants no additional rights in those images. See [ImageNet's copyright statement](https://www.image-net.org/about.php) and [access conditions](https://www.image-net.org/download.php).
- Software in this repository, including `utils.py`, is covered by the repository's [BSD 3-Clause license](../LICENSE).

## Citation

Please cite the MAD paper when using the dataset in research:

H. Chen, J. Jiang and N. Zheng, "Learning to Infer Unseen Single-/Multi-Attribute-Object Compositions With Graph Networks," *IEEE Transactions on Pattern Analysis and Machine Intelligence*. DOI: [10.1109/TPAMI.2023.3273712](https://doi.org/10.1109/TPAMI.2023.3273712).

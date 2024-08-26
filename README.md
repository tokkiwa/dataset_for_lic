# dataset_for_lic
Utility Scripts and Procedures for Preparing Dataset for Learned Image Compression

# TCM Dataset (Imagenet 300k images) 
Dataset used in the paper [Learned Image Compression with Mixed Transformer-CNN Architectures](https://arxiv.org/abs/2303.14978)
Official Repository: https://github.com/jmliu206/LIC_TCM

Download Imagenet repository and unzip. 
Imagenet: https://www.image-net.org/download.php (130GB)

Then, randomly choose 300k images. However, some images in Imagenet are less than size 256 and not suitable for training. 
So my script chooses the largest 300k images deterministicly. 

Here `root_dir` denotes the directory where the folder `imagenet-object-localization-challenge` is located.
For example, if your directory path looks like `/home/datasets/imagenet-object-localization-challenge/ILSVRC/Data/...`, then specify `/home/datasets`. 
The output directory is also made under `/home/datasets`.

```
python3 imagenet.py --root_dir /path/to/directory/
```

# MLIC++ Dataset (Imagenet + Flickr2k + DIV2k + CLIC + COCO)
Dataset used in the paper [MLIC ++ : Linear Complexity Multi-Reference Entropy Modeling for Learned Image Compression](https://arxiv.org/abs/2307.15421)
Official Repository: https://github.com/JiangWeibeta/MLIC

First, download each dataset and put them in some directory. 

Imagenet: https://www.image-net.org/download.php (130GB)
COCO: https://cocodataset.org/#download (81GB)
- Download **ALL** images; 2014 Train, 2014 Val, 2014 Test, 2015 Test, 2017 Train, 2017 Val, 2017 Test and 2017 Unlabeled.
Flickr 2k: https://www.kaggle.com/datasets/daehoyang/flickr2k (11GB)
- Note that this is not Flickr30k dataset or Flickr8k dataset!
CLIC: https://clic.compression.cc/2021/tasks/index.html
DIV2k: https://data.vision.ee.ethz.ch/cvl/DIV2K/
- Download two files labeled **High Resolution Images: Train Data (HR images), Validation Data (HR images)**

You can download train image list from (MLIC repo)[https://github.com/JiangWeibeta/MLIC]
Then, run `select.py` in this repository. 

```
python3 select.py --train_list_path /path/to/mlic/train/list --source_dir /path/to/directory/where/all/datas/stored \
--dest_dir /path/to/directory/where/output/will/be/stored
```

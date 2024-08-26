import os
import shutil
from PIL import Image

# 画像のサイズを取得する関数
def get_image_size(image_path):
    with Image.open(image_path) as img:
        return os.path.getsize(image_path)

# 画像を選択してコピーする関数
def select_and_copy_images(src_folder, dest_folder, num_images):
    # 画像ファイルのパスとサイズを取得
    image_files = []
    total_files = sum([len(files) for r, d, files in os.walk(src_folder)])
    processed_files = 0

    for root, _, files in os.walk(src_folder):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                file_path = os.path.join(root, file)
                image_size = get_image_size(file_path)
                image_files.append((file_path, image_size))
                processed_files += 1
                if processed_files % 100 == 0:
                    percent_done = processed_files / total_files * 100
                    print(f"processed {processed_files} image ({percent_done:.2f}%)")

    # サイズでソートして上位の画像を選択
    image_files.sort(key=lambda x: x[1], reverse=True)
    selected_images = image_files[:num_images]

    # 新しいフォルダにコピー
    os.makedirs(dest_folder, exist_ok=True)
    for i, (file_path, _) in enumerate(selected_images):
        dest_path = os.path.join(dest_folder, os.path.basename(file_path))
        shutil.copy(file_path, dest_path)
        if (i + 1) % 100 == 0:
            percent_done = (i + 1) / num_images * 100
            print(f"copied {i + 1} images ({percent_done:.2f}%)")

# フォルダパスの設定
import argparse
parser = argparse.ArgumentParser(description='Copy images from source directory to destination directory based on a list of image names.')
parser.add_argument('--rootpath', type=str, help='Path to root directory')
args = parser.parse_args()

rootpath = args.rootpath
src_train_folder = rootpath + 'ILSVRC/Data/CLS-LOC/train'
src_val_folder = rootpath + 'ILSVRC/Data/CLS-LOC/val'
dest_train_folder = rootpath + 'imagenet_sub300k/train'
dest_val_folder = rootpath + 'imagenet_sub300k/val'

# 画像を選択してコピー
select_and_copy_images(src_train_folder, dest_train_folder, 300000)
select_and_copy_images(src_val_folder, dest_val_folder, 50000)
import os
import shutil

def copy_images(train_list_path, source_dir, dest_dir):
    # train_list.txtのパスを読み込み
    with open(train_list_path, 'r') as file:
        image_names = file.read().splitlines()
    print(f"Found {len(image_names)} files")
    
    # 画像名から拡張子を取り除く
    image_names = [os.path.splitext(name)[0] for name in image_names]

    # コピー先ディレクトリが存在しない場合は作成
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    not_found_files = []

    # 画像をコピー
    for i, image_name in enumerate(image_names):
        found = False
        for root, _, files in os.walk(source_dir):
            for file in files:
                if os.path.splitext(file)[0] == image_name:
                    dest_file_path = os.path.join(dest_dir, file)
                    if not os.path.exists(dest_file_path):
                        shutil.copy(os.path.join(root, file), dest_dir)
                        print(f"Copy {root}/{file}")
                    else:
                        print(f"File already exists in destination: {dest_file_path}")
                    found = True
                    break
            if found:
                break
        if not found:
            print(f"File not found: {image_name}. Total missing files: {len(not_found_files)}")
            not_found_files.append(image_name)
        if (i + 1) % 100 == 0:
            print(f"Processed {i + 1}/{len(image_names)} files")

    # 見つからなかったファイルをログに出力
    if not_found_files:
        with open(os.path.join(dest_dir, 'not_found_files.log'), 'w') as log_file:
            for file_name in not_found_files:
                log_file.write(f"{file_name}\n")

# 使用例
train_list_path = 'f:\\dataset\\train_list.txt'
source_dir = 'f:\\dataset'
dest_dir = 'f:\\dataset\\selected_images'
copy_images(train_list_path, source_dir, dest_dir)
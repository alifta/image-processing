import sys
import os
from PIL import Image


def check_paths():
    if len(sys.argv) <= 1:
        print('Please enter the name of the image directory.')
        exit()
    else:
        img_dir = sys.argv[1]
        if len(sys.argv) >= 3:
            out_dir = sys.argv[2]
        else:
            out_dir = img_dir + '_new'
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        return img_dir, out_dir


def convert_img(img_dir, out_dir, img_type='png'):
    count = 0
    for img_file in os.listdir(img_dir):
        img_path = os.path.join(img_dir, img_file)
        img = Image.open(img_path)
        new_img_file = os.path.splitext(img_file)[0] + f'.{img_type}'
        img_path = os.path.join(out_dir, new_img_file)
        img.save(img_path, img_type)
        count += 1
    print(f'Converted {count} images.')


def main():
    img_dir, out_dir = check_paths()
    convert_img(img_dir, out_dir)


if __name__ == "__main__":
    main()

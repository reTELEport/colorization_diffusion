import os
import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('--folder_path', default='./color', type=str,
                    help='The folder path')


if __name__ == "__main__":
	args = parser.parse_args()
	dirs = os.listdir(args.folder_path + "/color")
	for dir_item in dirs:
		print(dir_item)
		image_file = Image.open(args.folder_path + "/color/" + dir_item) # open colour image
		image_file = image_file.convert('L') # convert image to black and white
		image_file.save(args.folder_path + "/gray/" + dir_item)
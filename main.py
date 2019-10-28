import cv2
from test import Detector
import os, glob, shutil
import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--dir', default=False, const=True, action='store_const', required=False,
	                    help='enable directory mode , else it will be at file mode.')
	parser.add_argument('input', help='the input file or directiry')
	parser.add_argument('output', help='the output file or drectiry')

	args = parser.parse_args()
	dir = args.dir
	input = args.input
	output = args.output
	D = Detector()
	if dir:
		for i, f in enumerate(glob.glob(input)):
			os.makedirs(output)
			f2 = output + '/' + os.path.basename(f)
			img = D.predict_from_file(f)
			D.save(img, f2)
			print(i, f)
	else:
		img = D.predict_from_file(input)
		D.save(img, output)
print('finish.')
if __name__ == '__main__':
	main()

from capture import Capture
from show import show, key

def f(o):
	from cv2 import (
		ADAPTIVE_THRESH_GAUSSIAN_C,
		THRESH_BINARY,
		adaptiveThreshold,
		medianBlur,
		cvtColor,
		COLOR_BGR2GRAY,
		erode,
		Laplacian,
		CV_64F
	)
	from numpy import (ones, uint8)
	o = adaptiveThreshold(
		medianBlur(cvtColor(o, COLOR_BGR2GRAY), 5), 255,
		ADAPTIVE_THRESH_GAUSSIAN_C,
		THRESH_BINARY, 11, 2
	)
	o = Laplacian(
		o, CV_64F
	)
	return o

def main():
	from argparse import ArgumentParser
	parser = ArgumentParser()
	parser.add_argument("path")
	args = parser.parse_args()
	
	cap = Capture(args.path)
	cap.set(f)
	
	while cap.opened:
		try:
			frame = cap.get()
			show(frame)
			if key('q'):
				break
		except KeyboardInterrupt:
			break
	cap.save()
	cap.end()

if __name__ == "__main__":
	main()

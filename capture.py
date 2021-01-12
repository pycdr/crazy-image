from cv2 import VideoCapture, imwrite, destroyAllWindows

class Capture:
	def __init__(self, path = ""):
		self.cap = VideoCapture(0)
		self.path = path
		self.opened = True
		self.set()
	def set(self, func = lambda x:x):
		self.changer = func
	def get(self):
		self.opened = self.cap.isOpened()
		ret, frame = self.cap.read()
		if ret:
			frame = self.changer(frame)
			self._frm = frame
			return frame
	def save(self, path = ""):
		if path:
			imwrite(path, self._frm)
		else:
			imwrite(self.path, self._frm)
	def end(self):
		self.cap.release()
		destroyAllWindows()

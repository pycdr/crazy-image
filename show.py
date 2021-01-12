from cv2 import imshow, waitKey

_title = "crazy-image"

show = lambda frm: imshow(_title, frm)
key = lambda k: waitKey(1) & 0xFF == ord(k)


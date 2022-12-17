import cv2
src = cv2.VideoCapture('PathtoTheVideoFile')
while True:
  succes, frame = src.read()
  frame = cv2.resize(frame,(650,400))
  cv2.imwrite("Destination",frame)
cv2.destroyAllWindows()

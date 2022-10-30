import os
from PIL import Image
from pytesseract import pytesseract
import cv2
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
path_to_Dataset="./Datasetbooks/"
pytesseract.tesseract_cmd = path_to_tesseract
def Extract_Text_From_Img(image_path):
	img = cv2.imread(image_path)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cv2.imwrite("duumy.png",img)
	text = pytesseract.image_to_string(img)
	print(text[:-1])
def rename():
	i = 0
	for filename in os.listdir(path_to_Dataset):
		my_dest ="image" + str(i) + ".jpeg"
		my_source =path_to_Dataset + filename
		my_dest =path_to_Dataset + my_dest
		os.rename(my_source, my_dest)
		i += 1

Extract_Text_From_Img('./bookspines/image4/book10.jpeg')
        
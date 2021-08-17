import xml.etree.ElementTree as ET
import os
path_ = '/home/manas/Desktop/dataset/train/annotations/'

for filename in os.listdir(path_):
	path_filename = path_+filename
	print(filename)
	mytree = ET.parse(path_filename)
	myroot = mytree.getroot()

	for paths in myroot.iter('path'):
		if '/content/gdrive/My Drive/Fluture_custom/ImageAI-master/dataset/train/' not in paths.text:
			paths.text = '/content/gdrive/My Drive/Fluture_custom/ImageAI-master/dataset/train/'+(paths.text).rpartition('\\')[2]

		print(paths.text)

	for folders in myroot.iter('folder'):
		folders.text = '/content/gdrive/My Drive/Fluture_custom/ImageAI-master/dataset/train'


	mytree.write(path_filename)


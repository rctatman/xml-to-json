# Python 3 only

# import modules we'll need 
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
import json
import glob

# for each .xml file...
for file in glob.glob('*.xml'):

    # get file name
    name = str.split(file, ".")[-2]

    # open the XML file, convert to json and dump into a new file
    with open(file, "r") as input:
        jsonOut = bf.data(fromstring(input.read()))
        with open(name + ".json","w+") as newFile:
            json.dump(jsonOut, newFile, ensure_ascii=False)

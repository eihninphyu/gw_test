import os
import csv
import json
from lxml import etree

def get_question1_dataset_directory():
    return os.getcwd()+"\\Dataset"

def get_csv_files(directory):
    csv_count = 0
    csv_files = []
    for path, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                csv_files.append(path+"\\"+file)
                csv_count += 1
    return csv_count,csv_files

def csv_to_json(csv_file, json_file):
    data ={}  
    count=0
    with open(csv_file, 'r') as csv_data:
        csv_reader = csv.reader(csv_data)
        for row in csv_reader:
            if len(row) == 5:
                count+=1
                x, y, width, height,tag = map(str,row[:5])
                formatted_record = "record-{:02}".format(count)
                data.update({
                    formatted_record:{
                        'x':x,
                        'y':y,
                        'width':width,
                        'height':height,
                        'tag':tag
                    }
                })                
    
    with open(json_file, 'w') as json_data:
        json_data.write(json.dumps(data, indent=4))

def csv_to_xml(csv_file, xml_file):
    root = etree.Element("annotation")
    with open(csv_file, 'r') as csv_data:
        csv_reader = csv.reader(csv_data)
        for row in csv_reader:
            x, y, width, height,tag = map(str,row[:5])  

            obj_element= etree.SubElement(root,"object") 

            element = etree.SubElement(obj_element, 'tag')
            element.text = tag

            bnd_element= etree.SubElement(obj_element,"bndbox")                     
            element = etree.SubElement(bnd_element, 'x')
            element.text = x
            element = etree.SubElement(bnd_element, 'y')
            element.text = y
            element = etree.SubElement(bnd_element, 'width')
            element.text = width
            element = etree.SubElement(bnd_element, 'height')
            element.text = height
    
    tree = etree.ElementTree(root)
    tree.write(xml_file, encoding="utf-8", xml_declaration=False,pretty_print=True)


from utils import get_csv_files,get_question1_dataset_directory,csv_to_xml

directory_path = get_question1_dataset_directory()
_,csv_files = get_csv_files(directory_path)

for file in csv_files:
    input_csv_file = file
    output_xml_file = file.replace(".csv",".xml")

    csv_to_xml(input_csv_file, output_xml_file)

    print(f"CSV file '{input_csv_file}' has been converted to XML file '{output_xml_file}'.")


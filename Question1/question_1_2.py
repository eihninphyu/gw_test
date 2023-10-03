from utils import get_csv_files,get_question1_dataset_directory,csv_to_json

directory_path = get_question1_dataset_directory()
_,csv_files = get_csv_files(directory_path)

for file in csv_files:
    input_csv_file = file
    output_json_file = file.replace(".csv",".json")

    csv_to_json(input_csv_file, output_json_file)

    print(f"CSV file '{input_csv_file}' has been converted to JSON file '{output_json_file}'.")


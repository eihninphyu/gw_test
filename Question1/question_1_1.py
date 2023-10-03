import os
from utils import get_question1_dataset_directory,get_csv_files

directory_path = get_question1_dataset_directory()

csv_file_count,_ = get_csv_files(directory_path)

print(f"CSV File Count: {csv_file_count} files")

import os
import argparse
import logging


logger = logging.getLogger(__name__)


SEPARATOR = ', Visited On '


def parse_arguments():
    parser = argparse.ArgumentParser(description="A Python program to remove duplicates from text files")
    parser.add_argument("--input-folder", required=True, help="Path to the input folder containing .txt files")
    parser.add_argument("--output-folder", required=True, help="Path to the output folder for writing results")
    return parser.parse_args()


def read_file_to_set(file_name):
    unique_lines = set()
    with open(file_name, 'r') as file:
        line_count = 0
        for line in file:
            line_strip = line.strip()
            if line_strip in unique_lines:
                print(f"Duplicate was found: {line_strip}")
            unique_lines.add(line_strip)
            line_count += 1

    return unique_lines, line_count


def extract_visit_time(url):
    parts = url.split(SEPARATOR)
    if len(parts) == 2:
        return parts[1]
    else:
        return ""


def write_set_to_file(file_name, unique_lines):
    with open(file_name, 'w') as file:
        for line in sorted(unique_lines):
            file.write(line + '\n')


def process_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    txt_files = [f for f in os.listdir(input_folder) if f.endswith(".txt")]

    for txt_file in txt_files:
        print(f"Processing file: {txt_file}")
        input_file_path = os.path.join(input_folder, txt_file)
        output_file_path = os.path.join(output_folder, txt_file)

        unique_lines, line_count_before = read_file_to_set(input_file_path)

        urls_list = sorted(unique_lines, key=extract_visit_time)

        write_set_to_file(output_file_path, urls_list)

        print(f"Number of lines. before: {line_count_before}, after: {len(urls_list)}\n")


if __name__ == "__main__":
    args = parse_arguments()
    input_folder = args.input_folder
    output_folder = args.output_folder

    print(f"Input folder: {input_folder}")
    print(f"Output folder: {output_folder}")

    print("File processing started.")

    process_files(input_folder, output_folder)

    print("Files processed and written to the output folder. DONE")

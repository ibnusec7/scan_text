import os
from colorama import init, Fore

init(autoreset=True)

def find_matching_words(file_content, target_contents):
    matching_words = []
    for target_content in target_contents:
        if target_content.lower() in file_content.lower():
            matching_words.append(target_content)
    return matching_words

def check_file_content(file_path, target_contents):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            return find_matching_words(content, target_contents)
    except Exception as e:
        print(f"Error: {e}")
        return []

def search_directory(root_directory, target_contents):
    found_files = []
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            file_path = os.path.join(root, file)
            matching_words = check_file_content(file_path, target_contents)
            if matching_words:
                matching_words_str = ', '.join(matching_words)
                print(f"File {file_path} contains '{Fore.GREEN}{matching_words_str}{Fore.RESET}'.")
                found_files.append(file_path)
    
    with open('result-scan.txt', 'w') as output_file:  
        for found_file in found_files:
            output_file.write(f"File {found_file} contains '{', '.join(target_contents)}'.\n")

root_directory = input("Enter the root directory path: ")
target_contents = input("Enter the target content(s) to search for (comma-separated): ").split(',')

search_directory(root_directory, target_contents)
print("Hasil disimpan dalam 'result-scan.txt'.")

import sys
from pathlib import Path

def list_recursively(input_list):
    dir_path = Path(input_list[1].strip('\"'))
    recursive_list = []
    if "-f" in input_list:
        pass
    else:
        for subpath in dir_path.iterdir():
            pass



def list_files(input_list):
    dir_path = Path(input_list[1].strip('\"'))
    subpath_list = []
    for subpath in dir_path.iterdir():
        if subpath.is_file():
            subpath_list.append(subpath)
    return subpath_list

def list_subpaths(input_list):
    dir_path = Path(input_list[1].strip('\"'))
    subpath_list = []
    for subpath in dir_path.iterdir():
        subpath_list.append(subpath)
    return subpath_list

def list_content(input_list):
    print(input_list)
    if not input_list[2]:
        list_subpaths(input_list)
    if "-r" in input_list[2]:
        pass
    if "-f" in input_list[2]:
        list_files(input_list)
    if "-s" in input_list[2]:
        pass



def find_file_and_extension(flags_set):
    file_and_extension = []
    for entry in flags_set:
        if "." in entry and entry[0] != "." and entry[-1] != "." and entry[0] != "-":
            file_and_extension.append(entry)
    if len(file_and_extension) == 0:
        file_and_extension.append("")
    for entry in flags_set:
        if len(entry) >= 2 and len(entry) <= 4 and entry.isalpha():
            file_and_extension.append(entry)
    if len(file_and_extension) == 1:
        file_and_extension.append("")
    return file_and_extension


def organize_flags(flags_set):
    flags_list = []
    file_and_extension = find_file_and_extension(flags_set)
    if "-r" in flags_set:
        flags_list.append("-r")
    if "-f" in flags_set:
        flags_list.append("-f")
    if "-s" in flags_set and len(file_and_extension[0]) > 0:
        flags_list.append("-s")
        flags_list.append(file_and_extension[0])
    elif "-e" in flags_set and len(file_and_extension[1]) > 0:
        flags_list.append("-e")
        flags_list.append(file_and_extension[1])
    return flags_list

def take_input():
    program_command = input("Enter 'Q' to exit or 'L' to list content of a directory: ")
    if program_command == "Q":
        sys.exit(0)
    directory = input("Enter a directory: ") #implement exception handling here
    flags_set = set()
    print("Here's a list of options for displaying directory content:\n Type '-r' to output directory content recursively\n Type '-f' to output only files\n Type '-s' followed by a file name to output files with that file name\n Type '-e' followed by a file extension to output files with that file extension\n Do not enter both '-s' and '-e'. If you do, '-s' will take priority.\nType 'done' to finish entering additional flags:")
    flag_input = input()
    while flag_input != "done":
        flags_set.add(flag_input)
        flag_input = input()
    flags_list = organize_flags(flags_set)
    input_list = []
    input_list.append(program_command)
    input_list.append(directory)
    input_list.append(flags_list)
    return input_list

def main():
    input_list = take_input()
    list_content(input_list)

if __name__ == "__main__":
    main()
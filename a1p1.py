import sys

def find_file_and_extension(flags_set):
    file_and_extension = []
    for entry in flags_set:
        if "." in entry and not entry[0] and not entry[-1]:
            file_and_extension.append(entry)
    if len(file_and_extension) == 0:
        file_and_extension.append("")
    for entry in flags_set:
        if len(entry) > 1 and len(entry) < 5:
            file_and_extension.append(entry)
    if len(file_and_extension) == 1:
        file_and_extension.append("")
    return file_and_extension


def organize_flags(flags_set):
    flags_list = []
    file_and_extension = file_and_extension(flags_set)
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

def take_input():
    program_command = input("Enter 'Q' to exit or 'L' to list content of a directory: ")
    if program_command == "Q":
        sys.exit(0)
    directory = input("Enter a directory: ")
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
    print(input_list)

if __name__ == "__main__":
    main()
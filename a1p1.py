import sys

def organize_flags(flags):
    pass

def take_input():
    program_command = input("Enter 'Q' to exit or 'L' to list content of a directory: ")
    if program_command == "Q":
        sys.exit(0)
    directory = input("Enter a directory: ")
    flags = set()
    print("Here's a list of options for displaying directory content:\n Type '-r' to output directory content recursively\n Type '-f' to output only files\n Type '-s' followed by a file name to output files with that file name\n Type '-e' followed by a file extension to output files with that file extension\nType 'done' to finish entering additional flags:")
    flag_input = input()
    while flag_input != "done":
        flags.add(flag_input)
        flag_input = input()
    flags = organize_flags(flags)
    input_list = []
    input_list.append(program_command)
    input_list.append(directory)
    input_list.append(flags)
    return input_list

def main():
    input_list = take_input()

if __name__ == "__main__":
    main()
import json
import sys


def load_json_file(filename):
    with open(filename) as json_data:
        d = json.load(json_data)
        print(d)
    return d


def open_file(filename):
    with open(filename, 'r') as my_file:
        d = my_file.read().replace('\n', '')
        print(d)
    return d


def get_lines(data):
    open_braces = 0
    is_comment = False
    for index, c in enumerate(data):
        if c == '"':
            is_comment = not is_comment
        elif not is_comment:
            if c == '{':
                open_braces += 1

            if c == '}':
                open_braces -= 1

    if open_braces == 0:
        return True
    else:
        return False


def json_parser(data):
    open_braces = 0
    close_braces = 0
    open_brackets = 0
    close_brackets = 0
    is_comment = False
    for index, c in enumerate(data):
        if c == '"':
            is_comment = not is_comment
        elif not is_comment:
            if c == '{':
                open_braces += 1
            if c == '}':
                close_braces += 1
                if open_braces == close_braces:
                    json1 = data[:index]
                    json2 = data[index:]
                    print(json1)
                    print(json2)
                    break
            if c == '[':
                open_brackets += 1
            if c == ']':
                close_brackets += 1

    return open_braces, close_braces, open_brackets, close_brackets


def main(filename):
    # json_data = load_json_file(filename)
    json_data = open_file(filename)
    is_json_valid = get_lines(str(json_data))
    if is_json_valid:
        print(json_data)
        open_braces, close_braces, open_brackets, close_brackets = json_parser(str(json_data))
        print(open_braces, close_braces, open_brackets, close_brackets)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Please add file path arg: {sys.argv[0]} <data_file_name>")
    else:
        main(sys.argv[1])

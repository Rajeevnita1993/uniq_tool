import sys

def uniq(input_lines, output_file=None, count=False, repeated=False, unique=False):
    unique_lines = []
    previous_line = None
    line_counts = []
    current_count = 1

    for line in input_lines:
        if line == previous_line:
            current_count += 1
        else:
            if previous_line is not None:
                unique_lines.append(previous_line)
                line_counts.append(current_count)
            previous_line = line
            current_count = 1

    if previous_line is not None:
        unique_lines.append(previous_line)
        line_counts.append(current_count)

    output_lines = []
    for i, line in enumerate(unique_lines):
        if unique and line_counts[i] > 1:
            continue
        if repeated and line_counts[i] == 1:
            continue
        if count:
            output_lines.append(f"{line_counts[i]} {line}")
        else:
            output_lines.append(line)

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(output_lines)           
    else:
        for line in output_lines:
            print(line, end='')



def main():
    if len(sys.argv) < 2:
        print("Usage: python uniq.py [-c|--count] [-d|--repeated] <input_file> [output_file]")
        sys.exit(1)

    count = False
    repeated = False
    unique = False
    arg_index = 1

    while arg_index < len(sys.argv) and sys.argv[arg_index].startswith('-'):
        options = sys.argv[arg_index][1:]
        #print("options: ", options)
        if 'c' in options:
            count = True
        if 'd' in options:
            repeated = True
        if 'u' in options:
            unique = True
        arg_index += 1
    
    if count or repeated or unique:
        updated_arg_index = arg_index
    else:
        updated_arg_index = 1

    input_file = sys.argv[updated_arg_index] if updated_arg_index < len(sys.argv) else '-'
    output_file = sys.argv[updated_arg_index + 1] if updated_arg_index + 1 < len(sys.argv) and sys.argv[updated_arg_index + 1] != '-' else None
    #print("input: ", input_file)
    #print("output: ", output_file)

    if input_file == '-':
        input_lines = sys.stdin.readlines()
    else:
        with open(input_file, 'r', encoding='utf-8') as file:
            input_lines = file.readlines()

    uniq(input_lines, output_file, count, repeated, unique)

if __name__ == "__main__":
    main()

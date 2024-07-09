import subprocess

def test_adjacent_duplicates():
    result = subprocess.run(['my_uniq', 'challenge-uniq/test.txt'], capture_output=True, text=True)
    expected_output = "line1\nline2\nline3\nline4\n"
    assert result.stdout == expected_output

def test_non_adjacent_duplicates():
    result = subprocess.run(['my_uniq', 'challenge-uniq/test_non_adjacent.txt'], capture_output=True, text=True)
    expected_output = "line1\nline2\nline1\nline3\nline1\nline4\nline5\nline2\nline3\n"
    assert result.stdout == expected_output

def test_read_from_stdin():
    input_data = "line1\nline2\nline2\nline3\nline4\n"
    result = subprocess.run(['my_uniq', '-'], input=input_data, capture_output=True, text=True)
    expected_output = "line1\nline2\nline3\nline4\n"
    assert result.stdout == expected_output

def test_read_from_stdin_write_to_file():
    input_data = "line1\nline2\nline2\nline3\nline4\n"
    with open('out.txt', 'w') as out_file:
        result = subprocess.run(['my_uniq', '-', 'out.txt'], input=input_data, capture_output=True, text=True)
    with open('out.txt', 'r') as out_file:
        output = out_file.read()

    expected_output = "line1\nline2\nline3\nline4\n"
    assert output == expected_output

def test_count_option():
    result = subprocess.run(['my_uniq', '-c', 'challenge-uniq/test.txt'], capture_output=True, text=True)
    expected_output = "1 line1\n2 line2\n1 line3\n1 line4\n"
    assert result.stdout == expected_output

def test_count_option_stdin():
    input_data = "line1\nline2\nline2\nline3\nline4\n"
    result = subprocess.run(['my_uniq', '-c', '-'], input=input_data, capture_output=True, text=True)
    expected_output = "1 line1\n2 line2\n1 line3\n1 line4\n"
    assert result.stdout == expected_output

def test_repeated_option():
    result = subprocess.run(['my_uniq', '-d', 'challenge-uniq/test.txt'], capture_output=True, text=True)
    expected_output = "line2\n"
    assert result.stdout == expected_output

def test_repeated_option_stdin():
    input_data = "line1\nline2\nline2\nline3\nline4\n"
    result = subprocess.run(['my_uniq', '-d', '-'], input=input_data, capture_output=True, text=True)
    expected_output = "line2\n"
    assert result.stdout == expected_output

def test_count_and_repeated_option():
    result = subprocess.run(['my_uniq', '-cd', 'challenge-uniq/test.txt'], capture_output=True, text=True)
    expected_output = "2 line2\n"
    assert result.stdout == expected_output

def test_count_and_repeated_option_stdin():
    input_data = "line1\nline2\nline2\nline3\nline4\n"
    result = subprocess.run(['my_uniq', '-cd', '-'], input=input_data, capture_output=True, text=True)
    expected_output = "2 line2\n"
    assert result.stdout == expected_output

def test_unique_option():
    result = subprocess.run(['my_uniq', '-u', 'challenge-uniq/test.txt'], capture_output=True, text=True)
    expected_output = "line1\nline3\nline4\n"
    assert result.stdout == expected_output

def test_unique_option_stdin():
    input_data = "line1\nline2\nline2\nline3\nline4\n"
    result = subprocess.run(['my_uniq', '-u', '-'], input=input_data, capture_output=True, text=True)
    expected_output = "line1\nline3\nline4\n"
    assert result.stdout == expected_output

def test_count_and_unique_option():
    result = subprocess.run(['my_uniq', '-cu', 'challenge-uniq/test.txt'], capture_output=True, text=True)
    expected_output = "1 line1\n1 line3\n1 line4\n"
    assert result.stdout == expected_output

def test_count_and_unique_option_stdin():
    input_data = "line1\nline2\nline2\nline3\nline4\n"
    result = subprocess.run(['my_uniq', '-cu', '-'], input=input_data, capture_output=True, text=True)
    expected_output = "1 line1\n1 line3\n1 line4\n"
    assert result.stdout == expected_output




    

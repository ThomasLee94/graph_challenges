def read_file(file_name):

    with open(file_name, "r") as opened_file:
        
        text = opened_file.read()
        split_text = text.split("\n")
        
        data = split_text[0], split_text[1].split(","), split_text[2:]

    return data
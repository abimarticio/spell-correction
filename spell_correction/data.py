def load_data(filename: str) -> list:
    with open(filename, "r") as text_file:
        data = text_file.readlines()
    return data
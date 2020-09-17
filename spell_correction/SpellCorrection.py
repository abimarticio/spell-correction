class SpellCorrection():
    def __init__(self, data:str):
        self.data = data

    def get_list(self) -> list:
        data = [line.strip("\n") for line in self.data]
        lines = [] 
        for line in data:
            new_line = line.split(":")
            lines.append(new_line)
        return lines

    def create_dictionary(self, lines: list) -> dict:
        corrections = {}
        for line in lines:
            key = line[0]
            values = line[1]
            values = values.strip()
            if "," in values:
                values = values.split(",")
                new_values = []
                for value in values:
                    value = value.strip()
                    new_values.append(value)
                    values = new_values
                    corrections[key] = values
            else:
                corrections[key] = values
        return corrections
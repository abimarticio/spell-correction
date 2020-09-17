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
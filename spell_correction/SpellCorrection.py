from .data import load_data

class SpellCorrection:
    def __init__(self, data: str):
        self.data = load_data(filename=data)

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

    def invert_dictionary(self, corrections: dict) -> dict:
        dictionary = {}
        for key, value in corrections.items():
            if isinstance(value, str):
                dictionary[value] = key
            elif isinstance(value, list):
                for element in value:
                    dictionary[element] = key
        return dictionary

    def get_correction(self, word: str) -> str:
        lines = self.get_list()
        corrections = self.create_dictionary(lines=lines)
        dictionary = self.invert_dictionary(corrections=corrections)
        correct_word = dictionary.get(word)
        return correct_word

    def get_batch_correction(self, words: list, dictionary: dict) -> list:
        correct_words = []
        for word in words:
            correct_word = self.get_correction(word=word, dictionary=dictionary)
            correct_words.append(correct_word)
        return correct_words

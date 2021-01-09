# Spell Correction Flask app
# Copyright (C) 2021  Abigail A. Marticio

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
        """
        Creates dictionary.

        Parameters
        ----------
        lines: list
            The data in list.

        Returns
        -------
        corrections: dict
            The data in dictionary where keys are the correct words and values are the mispelled words.
        """
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
        """
        Inverts the corrections dictionary.

        Parameters
        ----------
        corrections: dict
            The corrections dictionary where keys are the correct words and values are the mispelled words.

        Returns
        -------
        dictionary: dict
            The inverted dictionary where the keys are the mispelled words and the values are the correct words.
        """
        dictionary = {}
        for key, value in corrections.items():
            if isinstance(value, str):
                dictionary[value] = key
            elif isinstance(value, list):
                for element in value:
                    dictionary[element] = key
        return dictionary

    def get_correction(self, word: str) -> str:
        """
        Gets the correct word.

        Parameters
        ----------
        word: str
            The mispelled word.

        Returns
        -------
        str
            The correct word.
        """
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

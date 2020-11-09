from spell_correction import load_data, SpellCorrection


def main():
    data = load_data(filename="assets/spell-errors.txt")
    data = data[:50]
    sc = SpellCorrection(data=data)
    lines = sc.get_list()
    corrections = sc.create_dictionary(lines=lines)
    dictionary = sc.invert_dictionary(corrections=corrections)
    texts = ["rainning", "raning", "writtings", "forer"]
    correct_texts = sc.get_batch_correction(words=texts, dictionary=dictionary)
    for text, correct_text in zip(texts, correct_texts):
        print(f"{text} => {correct_text}")


if __name__ == "__main__":
    main()

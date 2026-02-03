import csv
import os
import sys


FILE_PATH = r"E:\Program Files\RobinData\PYTHON\RawData\NATO_ALPHABET_DATA.csv"


def load_nato_data(path):

    if not os.path.exists(path):
        print("❌ File not found!")
        sys.exit()

    try:
        with open(path, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            return {row[0]: row[1] for row in reader}

    except Exception as error:
        print("❌ Error:", error)
        sys.exit()


def convert_word(word, data):

    return [data[ch] for ch in word]


def main():

    print("\n🚀 NATO ALPHABET CONVERTER 🚀")
    print("Type a word or sentence to convert.")
    print("Type 'exit' to close the program.")
    print("---------------------------------\n")

    nato_data = load_nato_data(FILE_PATH)

    while True:

        user_input = input("Enter text: ").strip()

        if user_input.lower() == "exit":
            print("✅ Converter Closed. Goodbye!")
            break

        if not user_input.replace(" ", "").isalpha():
            print("❌ Please use only letters and spaces.")
            continue

        words = user_input.upper().split()

        try:
            for word in words:
                result = convert_word(word, nato_data)
                print(" ➜ ".join(result))

            print()

        except KeyError:
            print("❌ Some letters are missing in CSV.")


if __name__ == "__main__":
    main()

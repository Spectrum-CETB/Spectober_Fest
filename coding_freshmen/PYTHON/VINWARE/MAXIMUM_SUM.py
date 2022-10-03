def get_frequency_of_chars(string: str) -> dict:
    freq_table = {}
    for char in string:
        if char not in freq_table:
            freq_table[char] = 0
        freq_table[char] += 1
    return freq_table


def check_anagram(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    freq_str1, freq_str2 = get_frequency_of_chars(str1), get_frequency_of_chars(str2)

    return freq_str1 == freq_str2


def main():
    str1, str2 = input(), input()
    result = check_anagram(str1, str2)
    print(result)


if __name__ == "__main__":
    main()

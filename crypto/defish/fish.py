def fishify(s):
    if not s:
        return

    emoji = ["🐟", "🍣", "♓", "🐠", "🐡", "🎣", "🐬", "🎏"]
    encoded = []

    for char in s:
        char = ord(char)
        char_encoding = []

        for i in range(0, 8):
            if char & (2 ** (i+1)):
                char_encoding.append(emoji[i])

        encoded.append("".join(char_encoding))

    return encoded


if __name__ == "__main__":
    print('\n'.join(fishify("PbI6bI{fisH_Can_6e_DifFeRent}")))

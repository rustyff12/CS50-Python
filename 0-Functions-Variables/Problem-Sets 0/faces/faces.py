# Faces


# Main dunction to call on
def main():
    # Create a function called convert()
    def convert():
        # Adding emojis as variables from https://emojipedia.org/
        emoji_slight_smile = "🙂"
        emoji_slight_frown = "🙁"

        # adding variables for emoticons
        emoticon_slight_smile = ":)"
        emoticon_slight_frown = ":("

        # Variable called smile_input to take in user input
        emoji_input = input(str("Please enter some text with an emoticon: "))

        # if/else statement to determine emoji type
        # Edge case comes first ie multiple emojis
        if (
            emoticon_slight_smile in emoji_input
            and emoticon_slight_frown in emoji_input
        ):
            # replacing first emoji and adding the result to variable emoji_one
            emoji_one = emoji_input.replace(":)", emoji_slight_smile)
            # replacing second emoji, adding result to variable emoji_two
            emoji_two = emoji_one.replace(":(", emoji_slight_frown)
            return emoji_two
        elif emoticon_slight_smile in emoji_input:
            return emoji_input.replace(":)", emoji_slight_smile)
        elif emoticon_slight_frown in emoji_input:
            return emoji_input.replace(":(", emoji_slight_frown)
        else:
            # if there is no emoji it falls through if/else statement and just returns the original text
            return emoji_input

    # calling print on convert()
    print(convert())


# Calling main()
main()

# check50 cs50/problems/2022/python/faces

# submit50 cs50/problems/2022/python/faces

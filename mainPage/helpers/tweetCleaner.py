import preprocessor as pre
import re
import string
import emoji

def containsEmoji(word):
    for character in word:
        if character in emoji.UNICODE_EMOJI:
            return(True)
    return(False)

# <lack>
def punctuationRemover(text):

    # remove punctuation
    for punctuation in list(string.punctuation):
        text = text.replace(punctuation, " ")

    # remove emoji
    text = ' '.join(word for word in text.split() if not containsEmoji(word))

    # remove number
    text = ''.join([character for character in text if not character.isdigit()])

    return text
# </lack>

# clean twitter-specifics
def preCleaner(text):
    pre.set_options(pre.OPT.URL, pre.OPT.HASHTAG, pre.OPT.RESERVED, pre.OPT.MENTION)
    text = pre.clean(text)
    return text

# <lack>
def adjuster(text):

    # debug
    return text

    returnList = list()
    for word in text.split():
        returnList.append(word.strip("'").split("'")[0])
    returnString = " ".join(returnList)

    returnList = list()
    for word in returnString.split():
        returnList.append(word.strip("’").split("’")[0])
    returnString = " ".join(returnList)

    returnList = list()
    for word in returnString.split():
        returnList.append(word.strip("\"").split("\"")[0])

    # remainings
    remainings = ["xd","th"]

    returnString = " ".join([c for c in returnList if len(c) > 1 and\
                             c.lower() not in remainings and c[0] != "#"])
    returnString = returnString.lower().replace("i̇","i").strip()
    return returnString
# </lack>

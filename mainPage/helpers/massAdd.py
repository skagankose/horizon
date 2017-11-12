from .userRetriever import *
import os

def main():
    try:
        # <block>
        # load core users
        userNameList = []
        currentPath = os.path.dirname(os.path.realpath(__file__))
        f = open(currentPath + "/data/sampleUsers.txt", "rt")
        for user in f:
            userNameList.append(user.strip("\n"))
        f.close()
        # </block>

        # <block>
        # retrieve users and tweets
        for userName in userNameList:
            getUser(userName)
            getTweet(userName)
        # </block>

        return("All accounts are added succesfully.")

    except Exception as error:
        return("%s" % error)

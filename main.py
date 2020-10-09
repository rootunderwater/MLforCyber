import re
from os import listdir, walk
def getListOfTokens(path):
    emailText = open(path).readlines()[2:]
    regEx = re.compile('\W')
    listOfTokens = []
    for line in emailText:
        for word in regEx.split(line):
            if (len(word) >= 1):
                listOfTokens.append(word)
    return listOfTokens

def getFilespath(path):
    traningHamFilesPath = []
    traningSpamFilesPath = []
    testHamFilesPath = []
    testSpamFilesPath = []
    for (dirpath, dirnames, filenames) in walk('data'):
        if (dirpath.endswith('10')):
            for filename in filenames:
                if (filename.startswith('spm')):
                    testSpamFilesPath.append(dirpath + '/' + filename)
                else:
                    testHamFilesPath.append(dirpath + '/' + filename)
        elif (dirpath.startswith('p', 5,6)):
            for filename in filenames:
                if (filename.startswith('spm')):
                    traningSpamFilesPath.append(dirpath + '/' + filename)
                else:
                    traningHamFilesPath.append(dirpath + '/' + filename)
    return traningHamFilesPath, traningSpamFilesPath, testHamFilesPath, testSpamFilesPath
                    
        
    return filesPath
# path = 'data/part1/3-1msg2.txt'
path = 'data'
traningHamFilesPath, traningSpamFilesPath, testHamFilesPath, testSpamFilesPath = getFilespath(path)
print(traningHamFilesPath[:5], '\n', traningSpamFilesPath[:5],'\n', testHamFilesPath[:5],'\n', testSpamFilesPath[:5], '\n')

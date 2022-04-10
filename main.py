from enum import Enum

class Actions(Enum):
    Delete = 'D'
    Insert = 'I'
    Match = 'M'
    Replace = 'R'

def GetEditorialPrescription(str1, str2):
    M = len(str1)+1
    N = len(str2)+1
    D = [[0 for n in range(N)] for m in range(M)]
    for j in range(1, N):
        D[0][j] = D[0][j - 1] + 1
    for i in range(1, M):
        D[i][0] = D[i - 1][0] + 1
        for j in range(1, N):
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + (0 if str1[i-1] == str2[j-1] else 1))

    i = len(str1)
    j = len(str2)
    result = []
    while (i > 0) or (j > 0):
        _min = i + j
        pos = (0, 0)
        action = '_'
        if (i > 0):
            _min = D[i-1][j]
            pos = (i-1, j)
            action = Actions.Delete
        if (j > 0) and (D[i][j-1] <= _min):
            _min = D[i][j-1]
            pos = (i, j-1)
            action = Actions.Insert
        if (i > 0) and (j > 0) and (D[i-1][j-1] <= _min):
            pos = (i-1, j-1)
            if D[i-1][j-1] == D[i][j]:
                action = Actions.Match
            else:
                action = Actions.Replace
        i, j = pos
        result = [action] + result
    return result

def Main():
    str1 = input()
    str2 = input()
    print(GetEditorialPrescription(str1, str2))

if __name__ == '__main__':
    try:
        Main()
    except Exception as e:
        print(e)
        input()

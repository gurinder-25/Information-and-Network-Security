class PlayfairCipher:
    def __init__(self, key):
        self.key = key.lower()
        self.list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.matrix = self.generateKeyTable()
    def Diagraph(self, text):
        Diagraph = []
        group = 0
        for i in range(2, len(text), 2):
            Diagraph.append(text[group:i])
            group = i
        Diagraph.append(text[group:])
        return Diagraph

    def FillerLetter(self, text):
        k = len(text)
        if k % 2 == 0:
            for i in range(0, k, 2):
                if text[i] == text[i + 1]:
                    new_word = text[0:i + 1] + 'x' + text[i + 1:]
                    new_word = self.FillerLetter(new_word)
                    break
                else:
                    new_word = text
        else:
            for i in range(0, k - 1, 2):
                if text[i] == text[i + 1]:
                    new_word = text[0:i + 1] + 'x' + text[i + 1:]
                    new_word = self.FillerLetter(new_word)
                    break
                else:
                    new_word = text
        return new_word

    def generateKeyTable(self):
        key_letters = []
        for i in self.key:
            if i not in key_letters:
                key_letters.append(i)

        compElements = key_letters + [i for i in self.list1 if i not in key_letters]

        matrix = []
        while compElements:
            matrix.append(compElements[:5])
            compElements = compElements[5:]

        return matrix

    def search(self, mat, element):
        for i in range(5):
            for j in range(5):
                if mat[i][j] == element:
                    return i, j

    def encrypt_RowRule(self, matr, e1r, e1c, e2r, e2c):
        char1 = matr[e1r][(e1c + 1) % 5]
        char2 = matr[e2r][(e2c + 1) % 5]
        return char1, char2

    def encrypt_ColumnRule(self, matr, e1r, e1c, e2r, e2c):
        char1 = matr[(e1r + 1) % 5][e1c]
        char2 = matr[(e2r + 1) % 5][e2c]
        return char1, char2

    def encrypt_RectangleRule(self, matr, e1r, e1c, e2r, e2c):
        char1 = matr[e1r][e2c]
        char2 = matr[e2r][e1c]
        return char1, char2


    def encryptByPlayfairCipher(self, plainList):
        CipherText = []
        for i in range(len(plainList)):
            ele1_x, ele1_y = self.search(self.matrix, plainList[i][0])
            ele2_x, ele2_y = self.search(self.matrix, plainList[i][1])

            if ele1_x == ele2_x:
                c1, c2 = self.encrypt_RowRule(self.matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            elif ele1_y == ele2_y:
                c1, c2 = self.encrypt_ColumnRule(self.matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            else:
                c1, c2 = self.encrypt_RectangleRule(self.matrix, ele1_x, ele1_y, ele2_x, ele2_y)

            CipherText.append(c1 + c2)
        return CipherText

    def encrypt(self, text):
        text = text.lower().replace(" ", "")
        plainTextList = self.Diagraph(self.FillerLetter(text))
        if len(plainTextList[-1]) != 2:
            plainTextList[-1] += 'x'

        cipherList = self.encryptByPlayfairCipher(plainTextList)
        return ''.join(cipherList)


# Example usage:
key = "RANCHO"
text = "THREE IDIOTS"
cipher = PlayfairCipher(key)
cipherText = cipher.encrypt(text)
print("Key text:", key)
print("Plain Text:", text)
print("CipherText:", cipherText)


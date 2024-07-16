def CeaeserCipher(s, operation):
        res = []
        for i in range(len(s)):
            if s[i] == ' ':
                res.append(' ')
            elif operation == 'en':
                res.append(chr((ord(s[i]) - 97 + 3) % 26 + 97))
            elif operation == 'de':
                res.append(chr((ord(s[i]) - 97 - 3) % 26 + 97))
        return ''.join(res)

s = "the quick brown fox"
s1 = CeaeserCipher(s, 'en')
print("Encryption: ", s1)
print("Decryption: ", CeaeserCipher(s1, 'de'))

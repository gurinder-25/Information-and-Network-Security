import numpy as np

class HillCipher:
    def __init__(self, plaintxt, keyString):
        self.alphabet = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)}
        self.reverse = {v: k for k, v in self.alphabet.items()}
        self.plaintxt = plaintxt
        self.keyMatrix = self.create_key_matrix(keyString, 2)
        self.invKeyMatrix = self.find_inverse_key_matrix(self.keyMatrix)

    def create_key_matrix(self, key_string, size=2):
        key_values = [self.alphabet[char] for char in key_string]
        filler_values = [self.alphabet[chr(i)] for i in range(ord('a'), ord('a') + size * size)]
        combined_values = key_values + filler_values
        combined_values = combined_values[:size * size]
        key_matrix = [combined_values[i * size:(i + 1) * size] for i in range(size)]
        return key_matrix

    def list_to_matrix_pairs(self, lst):
        return [[lst[i], lst[i + 1]] for i in range(0, len(lst), 2)]

    def find_inverse_key_matrix(self, key_matrix):
        det = int(round(np.linalg.det(key_matrix)))
        det_inv = pow(det, -1, 26)
        adjugate = np.linalg.inv(key_matrix).T * det
        inv_key_matrix = (det_inv * adjugate) % 26
        inv_key_matrix = inv_key_matrix.astype(int)
        return inv_key_matrix

    def encrypt(self):
        List1 = [self.alphabet[i] for i in self.plaintxt]
        res = []
        matrix_pairs = self.list_to_matrix_pairs(List1)

        for pair in matrix_pairs:
            c = np.dot(self.keyMatrix, pair)
            for i in c:
                res.append(self.reverse[i % 26])
        return ''.join(res)

    def decrypt(self, ciphertext):
        List1 = [self.alphabet[i] for i in ciphertext]
        res = []
        matrix_pairs = self.list_to_matrix_pairs(List1)

        for pair in matrix_pairs:
            p = np.dot(self.invKeyMatrix, pair)
            for i in p:
                res.append(self.reverse[i % 26])
        return ''.join(res)

# Example usage
h = HillCipher('attack', 'cddg')
encrypted = h.encrypt()
print('Encrypted:', encrypted)
decrypted = h.decrypt(encrypted)
print('Decrypted:', decrypted)

from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            output_letter = (letter_index + key) % alphabet_len
            encrypted_text.append(self.alphabet[output_letter])
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        decrypted_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            output_letter = (letter_index - key) % alphabet_len
            decrypted_text.append(self.alphabet[output_letter])
        return "".join(decrypted_text)
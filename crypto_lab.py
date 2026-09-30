"""Educational Caesar cipher and XOR demonstrations; not production encryption."""


def caesar_encrypt(text, key):
    """Shift English letters; preserve case, punctuation and other characters."""
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
        elif 'A' <= char <= 'Z':
            start = ord('A')
        else:
            result.append(char)
            continue
        result.append(chr(start + (ord(char) - start + key) % 26))
    return ''.join(result)


def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)


def brute_force(text):
    """Return all 26 possible shifts; a human identifies plausible plaintext."""
    return [(key, caesar_decrypt(text, key)) for key in range(26)]


def text_to_binary(text):
    """Encode as UTF-8 so every output chunk is exactly one byte."""
    return ' '.join(format(byte, '08b') for byte in text.encode('utf-8'))


def binary_xor(first, second):
    # Permit spaces between bytes, but reject characters other than 0 and 1.
    first = ''.join(first.split())
    second = ''.join(second.split())
    if not first or not second or set(first + second) - {'0', '1'}:
        raise ValueError('Enter non-empty binary strings containing only 0 and 1.')
    if len(first) != len(second):
        raise ValueError('Binary strings must have the same number of bits.')
    return ''.join('0' if a == b else '1' for a, b in zip(first, second))


def xor_bytes(message, key):
    if not message or len(message) != len(key):
        raise ValueError('Message and key must be non-empty and have equal byte lengths.')
    return bytes(a ^ b for a, b in zip(message, key))


def main():
    print('PYTHON CRYPTOGRAPHY LAB — educational examples')
    while True:
        print('\n1 Encrypt Caesar\n2 Decrypt Caesar\n3 Try all Caesar keys')
        print('4 Text to binary\n5 Binary XOR\n6 Text XOR demo\n7 Decrypt text XOR\n0 Exit')
        try:
            choice = input('Choose an option: ').strip()
            if choice == '0':
                break
            if choice in {'1', '2'}:
                text = input('Message: ')
                key = int(input('Integer shift: '))
                function = caesar_encrypt if choice == '1' else caesar_decrypt
                print('Result:', function(text, key))
            elif choice == '3':
                for key, text in brute_force(input('Ciphertext: ')):
                    print(f'Key {key:2}: {text}')
            elif choice == '4':
                print('UTF-8 binary:', text_to_binary(input('Text: ')))
            elif choice == '5':
                print('Result:', binary_xor(input('Binary message: '), input('Binary key: ')))
            elif choice == '6':
                message = input('Text message: ').encode('utf-8')
                key = input('Text key (same UTF-8 byte length): ').encode('utf-8')
                print('Ciphertext in hexadecimal:', xor_bytes(message, key).hex())
            elif choice == '7':
                encrypted = bytes.fromhex(input('Ciphertext in hexadecimal: '))
                key = input('Original text key: ').encode('utf-8')
                print('Plaintext:', xor_bytes(encrypted, key).decode('utf-8'))
            else:
                print('Choose an option from 0 to 7.')
        except (ValueError, UnicodeError) as error:
            print('Input error:', error)
        except (EOFError, KeyboardInterrupt):
            print('\nFinished.')
            break


if __name__ == '__main__':
    main()

# Python Cryptography Lab

A learning project based on my Applied Cryptography Seminar 3 exercises: Caesar encryption and decryption, trying every Caesar key, converting text to binary, and demonstrating XOR.

## Attribution

The original exercises and starter code came from university seminar materials. Arica Bhuiyan worked on the seminar tasks; this standalone edition was corrected. It is an adaptation of coursework rather than an independently designed cryptographic system.

## Run

Requires Python.

Open a terminal in this folder and run:

```bash
python3 crypto_lab.py
```

On Windows, use `python crypto_lab.py` if needed.

Choose a menu option, enter the requested values, and select `0` to finish.

In a Carnets notebook with this file in the working folder, try:

```python
%run crypto_lab.py
```

The revised program was checked with Python, but has not been tested in Carnets.

## Examples

| Feature | Input | Result |
|---|---|---|
| Caesar encryption | `arica`, shift `2` | `ctkec` |
| Caesar decryption | `ctkec`, shift `2` | `arica` |
| Text to binary | `a` | `01100001` |
| Binary XOR | `01100001` and `01110000` | `00010001` |
| Text XOR encryption | message `arica`, key `peopl` | hexadecimal `111706130d` |

For text XOR decryption, enter `111706130d` and the original key `peopl` to recover `arica`.

## What I learned

- Functions, loops and conditional logic.
- Modulo arithmetic for wrapping around the alphabet.
- How `ord()` and `chr()` connect characters and numerical values.
- Encoding text as UTF-8 bytes.
- XOR and why applying the same key twice recovers the original bytes.
- Input validation and error handling.

## Corrections to the seminar attempt

### Caesar decryption

The correct expression adds the alphabet's starting value after shifting backwards:

```python
chr(start + (ord(char) - start - key) % 26)
```

The earlier expression subtracted from `start`, producing symbols rather than the intended letters.

The English alphabet has **26 letters**. `range(26)` tries keys 0 through 25. Key 0 leaves `arica` unchanged; key 1 gives `zqhbz`. Trying all shifts lists candidates; it does not automatically determine the correct message.

This edition shifts only English letters. It preserves case, punctuation and non-English characters.

### Binary and XOR

The original XOR cell accepted ordinary words as though they were binary. This edition rejects anything other than binary digits and whitespace. Its text XOR demonstration converts both the message and the key to bytes first, avoiding the earlier undefined or stale `binary_message` variable.

`ord()` returns a Unicode code point, not always an ASCII value. This edition uses UTF-8 encoding so the binary display consists of actual eight-bit bytes. Text keys need equal **byte lengths**, which may differ from character counts.

## XOR demo versus a one-time pad

A manually chosen text key such as `peopl` is a demonstration of XOR, not a secure one-time pad. A true one-time pad requires a uniformly random secret key as long as the message, used only once. This program does not manage those conditions.

Caesar and this text key XOR demo are educational tools and should not be used to protect passwords or private information.


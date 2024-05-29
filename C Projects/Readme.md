
# Cryptography Project

This is a simple command-line program written in C that implements three common cryptographic algorithms: Caesar Cipher, Substitution Cipher, and XOR Cipher.

## Description

The program prompts the user to choose one of the three available cryptographic algorithms. After selecting an algorithm, the user is asked to provide the plaintext (the original message) and any additional required input, such as the shift value for the Caesar Cipher or the key for the Substitution Cipher and XOR Cipher.

The program then encrypts the plaintext using the chosen algorithm and displays the resulting ciphertext (the encrypted message) to the console.

## Usage

1. Compile the code using a C compiler (e.g., `gcc` on Linux/macOS or Visual Studio on Windows).
2. Run the compiled executable.
3. Follow the prompts to choose the cryptographic algorithm, enter the plaintext, and provide any additional necessary input.
4. The program will display the ciphertext.

Here's an example usage scenario:

```
Enter your choice:
1. Caesar Cipher
2. Substitution Cipher
3. XOR Cipher
1
Enter the plaintext: Hello, World!
Enter the shift value: 3
Ciphertext: Khoor, Zruog!
```

In this example, the Caesar Cipher algorithm is chosen (option 1), the plaintext is `"Hello, World!"`, and the shift value is 3. The program encrypts the plaintext and displays the ciphertext `"Khoor, Zruog!"`.

## Algorithms

### 1. Caesar Cipher

The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is replaced by a letter a fixed number of positions down the alphabet.

### 2. Substitution Cipher

The Substitution Cipher is a cipher where each letter in the plaintext is replaced by a different letter based on a key. The key is a permutation of the alphabet.

### 3. XOR Cipher

The XOR Cipher is a simple encryption method where each character in the plaintext is XORed with a key character, and the key is repeated cyclically.

## Limitations

This implementation is a basic example for educational purposes and does not handle input validation, edge cases, or more advanced cryptographic techniques. Real-world cryptographic systems require much more robust and secure algorithms, key management, and other security measures.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

```



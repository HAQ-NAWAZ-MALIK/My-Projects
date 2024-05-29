#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Caesar Cipher
void caesarCipher(char *plaintext, char *ciphertext, int shift) {
    int i;
    for (i = 0; plaintext[i] != '\0'; i++) {
        if (isalpha(plaintext[i])) {
            char base = isupper(plaintext[i]) ? 'A' : 'a';
            ciphertext[i] = (plaintext[i] - base + shift) % 26 + base;
        } else {
            ciphertext[i] = plaintext[i];
        }
    }
    ciphertext[i] = '\0';
}

// Substitution Cipher
void substitutionCipher(char *plaintext, char *ciphertext, char *key) {
    int i;
    for (i = 0; plaintext[i] != '\0'; i++) {
        if (isalpha(plaintext[i])) {
            char base = isupper(plaintext[i]) ? 'A' : 'a';
            ciphertext[i] = key[tolower(plaintext[i]) - base];
            if (isupper(plaintext[i])) {
                ciphertext[i] = toupper(ciphertext[i]);
            }
        } else {
            ciphertext[i] = plaintext[i];
        }
    }
    ciphertext[i] = '\0';
}

// XOR Cipher
void xorCipher(char *plaintext, char *ciphertext, char *key) {
    int i, j = 0;
    int keyLen = strlen(key);
    for (i = 0; plaintext[i] != '\0'; i++) {
        ciphertext[i] = plaintext[i] ^ key[j];
        j = (j + 1) % keyLen;
    }
    ciphertext[i] = '\0';
}

int main() {
    char plaintext[100], ciphertext[100], key[27];
    int choice, shift;

    printf("Enter your choice:\n1. Caesar Cipher\n2. Substitution Cipher\n3. XOR Cipher\n");
    scanf("%d", &choice);

    printf("Enter the plaintext: ");
    scanf("%s", plaintext);

    switch (choice) {
        case 1:
            printf("Enter the shift value: ");
            scanf("%d", &shift);
            caesarCipher(plaintext, ciphertext, shift);
            printf("Ciphertext: %s\n", ciphertext);
            break;
        case 2:
            printf("Enter the key (26 characters): ");
            scanf("%s", key);
            substitutionCipher(plaintext, ciphertext, key);
            printf("Ciphertext: %s\n", ciphertext);
            break;
        case 3:
            printf("Enter the key: ");
            scanf("%s", key);
            xorCipher(plaintext, ciphertext, key);
            printf("Ciphertext: %s\n", ciphertext);
            break;
        default:
            printf("Invalid choice!\n");
    }

    return 0;
}
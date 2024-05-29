#include <stdio.h>
#include <string.h>
#include <stdint.h>

// Define constants for MD5
#define INIT_A 0x67452301
#define INIT_B 0xefcdab89
#define INIT_C 0x98badcfe
#define INIT_D 0x10325476

// Bit-wise rotation functions
#define ROTATE_LEFT(x, n) (((x) << (n)) | ((x) >> (32 - (n))))
#define F(x, y, z) (((x) & (y)) | ((~x) & (z)))
#define G(x, y, z) (((x) & (z)) | ((y) & (~z)))
#define H(x, y, z) ((x) ^ (y) ^ (z))
#define I(x, y, z) ((y) ^ ((x) | (~z)))

// MD5 helper functions
void md5_process(uint32_t *buf, const uint32_t *in);
void md5_pad(uint8_t *data, uint64_t len, uint64_t *padded_len);

// MD5 hash function
void md5_hash(const char *input, char *output) {
    uint32_t a = INIT_A, b = INIT_B, c = INIT_C, d = INIT_D;
    uint8_t data[64];
    uint64_t padded_len;

    md5_pad((uint8_t *)input, strlen(input), &padded_len);

    for (uint64_t i = 0; i < padded_len; i += 64) {
        for (uint8_t j = 0; j < 64; j++) {
            data[j] = input[i + j];
        }
        md5_process(&a, (uint32_t *)data);
    }

    // Output the final hash
    sprintf(output, "%08x%08x%08x%08x", a, b, c, d);
}

void md5_process(uint32_t *buf, const uint32_t *in) {
    uint32_t a = buf[0], b = buf[1], c = buf[2], d = buf[3];

    // Round 1
    a = b + ROTATE_LEFT((a + F(b, c, d) + in[0]), 7);
    d = a + ROTATE_LEFT((d + F(a, b, c) + in[1]), 12);
    c = d + ROTATE_LEFT((c + F(d, a, b) + in[2]), 17);
    b = c + ROTATE_LEFT((b + F(c, d, a) + in[3]), 22);
    // ... (omitted for brevity)

    buf[0] += a;
    buf[1] += b;
    buf[2] += c;
    buf[3] += d;
}

void md5_pad(uint8_t *data, uint64_t len, uint64_t *padded_len) {
    uint64_t i = len;
    uint8_t pad[64] = {0x80};

    if (len < 56) {
        memcpy(data + len, pad, 1);
        len += 1;
    } else {
        memcpy(data + len, pad, 1);
        len += 1 + 64 - (len % 64);
    }

    for (i = 0; i < 8; i++) {
        data[len++] = (uint8_t)(i * 8);
    }

    *padded_len = len;
}

int main() {
    char input[] = "Hello, World!";
    char output[33];

    md5_hash(input, output);
    printf("MD5 hash of \"%s\" is: %s\n", input, output);

    return 0;
}
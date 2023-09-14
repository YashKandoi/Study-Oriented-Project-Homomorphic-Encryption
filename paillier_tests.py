from paillier_implementation import PrivateKey, PublicKey, generate_keys, Encrypt, Decrypt, homomorphic_add, homomorphic_add_constant, homomorphic_mult_constant


def main():
    # Generate Paillier key pair
    public_key, private_key = generate_keys(bitlen=128)

    # Encrypt some plaintext
    plaintext1 = 42
    ciphertext1 = Encrypt(public_key, plaintext1)

    plaintext2 = 17
    ciphertext2 = Encrypt(public_key, plaintext2)

    # Perform homomorphic addition of encrypted values
    result_add = homomorphic_add(public_key, ciphertext1, ciphertext2)

    # Perform homomorphic addition with a constant
    constant = 5
    result_add_constant = homomorphic_add_constant(public_key, ciphertext1, constant)

    # Perform homomorphic multiplication with a constant
    constant_mult = 3
    result_mult_constant = homomorphic_mult_constant(public_key, ciphertext1, constant_mult)

    # Decrypt the results
    decrypted_result_add = Decrypt(public_key, private_key, result_add)
    decrypted_result_add_constant = Decrypt(public_key, private_key, result_add_constant)
    decrypted_result_mult_constant = Decrypt(public_key, private_key, result_mult_constant)

    # Display the results
    print("Plaintext 1:", plaintext1)
    print("Plaintext 2:", plaintext2)
    print("Ciphertext 1:", ciphertext1)
    print("Ciphertext 2:", ciphertext2)
    print("Homomorphic Addition Result:", decrypted_result_add)
    print("Homomorphic Addition with Constant Result:", decrypted_result_add_constant)
    print("Homomorphic Multiplication with Constant Result:", decrypted_result_mult_constant)

if __name__ == "__main__":
    main()
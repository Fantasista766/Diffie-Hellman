# Diffie-Hellman Key Exchange Protocol

## Introduction

This Python code demonstrates the implementation of the Diffie-Hellman key exchange protocol. The Diffie-Hellman key exchange is a method used to securely exchange cryptographic keys over a public channel. It allows two parties to generate a shared secret key without ever transmitting the key over the communication channel.

## Requirements

To run this code, you need the following Python libraries:

- `Crypto`: This library provides cryptographic functionality, including SHA512 hashing, HKDF key derivation, and random number generation.
- `uuid`: This library is used for generating unique identifiers.

You can install these libraries using pip:

```
pip install pycryptodome
```

## Usage

To use the Diffie-Hellman key exchange protocol, follow these steps:

1. **Instantiate Users**: Create two instances of the `DiffieHellmanUser` class, representing the two parties involved in the key exchange.

2. **Generate Keys**: Each user generates their public key using the `generate_key` method.

3. **Exchange Keys**: Users exchange their public keys with each other.

4. **Derive Common Key**: Upon receiving the other party's public key, each user derives a common key using the `receive_key` method.

5. **Check Common Key**: Finally, verify that both parties have derived the same common key.

## Code Structure

- `DiffieHellmanUser`: This class represents a user participating in the Diffie-Hellman key exchange. It contains methods for key generation and common key derivation.

- `run_protocol`: This function simulates the execution of the Diffie-Hellman key exchange protocol between two users.

- `main`: This is the entry point of the program. It calls the `run_protocol` function to execute the key exchange.

## System Parameters

- `PRIME_BIT_SIZE`: The bit size of the prime number used in the Diffie-Hellman protocol. In this code, it is set to 512 bits.

- `KEY_LENGTH`: The length of the derived common key in bytes. It is set to 32 bytes.

- `HKDF_MASTER`: The master key used for key derivation using HKDF. It is set to a byte string of length 16.
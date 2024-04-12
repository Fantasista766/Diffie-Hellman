from Crypto.Hash import SHA512
from Crypto.Protocol.KDF import HKDF
from Crypto.Random import random
from Crypto.Util.number import getStrongPrime
from Crypto.Util.number import long_to_bytes

import uuid

# System parameters
PRIME_BIT_SIZE = 512
KEY_LENGTH = 32
HKDF_MASTER = b'\x00' * 16


class DiffieHellmanUser:
    def __init__(self, p, g, _id=None):
        """Initialize a Diffie-Hellman user.

        Args:
            p (int): Prime number p.
            g (int): Generator g.
            _id (uuid.UUID): Unique ID of the user. If not provided, a new UUID is generated.
        """
        self.p = p
        self.g = g
        self.id = uuid.uuid4() if not _id else _id  # unique ID for the user
        self.exp = random.randint(1, self.p - 1)  # private exponent
        self.common_key = None  # shared secret key
        print(f'[Diffie-Hellman User], ID {self.id}:\nUser has been created\n')

    def generate_key(self):
        """Generate the public key."""
        print(f'[Diffie-Hellman User], ID {self.id}:\nPublic key has been generated\n')
        return pow(self.g, self.exp, self.p)

    def receive_key(self, other_key):
        """Receive the other participant's public key and generate the common key."""
        print(f'[Diffie-Hellman User], {self.id}:\nEstablishing common key...')
        w = pow(other_key, self.exp, self.p)  # shared secret
        self.common_key = HKDF(HKDF_MASTER, KEY_LENGTH, long_to_bytes(w), SHA512, 1)  # derived common key
        print(f'Generated common key: {self.common_key.hex()}\n')
        return self.common_key


def run_protocol():
    # generate prime number and random generator
    p = getStrongPrime(PRIME_BIT_SIZE)
    g = random.randint(2, p - 1)

    # create two Diffie-Hellman users
    user_a = DiffieHellmanUser(p, g)
    user_b = DiffieHellmanUser(p, g)

    # generate public keys for both users
    u = user_a.generate_key()
    v = user_b.generate_key()

    # exchange public keys and derive common keys
    key_a = user_a.receive_key(v)
    key_b = user_b.receive_key(u)

    # check if the common keys match
    if key_a == key_b:
        print('Common key has been established successfully!')
    else:
        raise Exception('An error occurred during establishing common key!')


def main():
    run_protocol()


if __name__ == '__main__':
    main()

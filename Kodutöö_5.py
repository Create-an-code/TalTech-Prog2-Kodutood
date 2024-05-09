import random
from sympy import mod_inverse, gcd

# Funktsioon suurte algarvude genereerimiseks
def generate_large_prime():
    return random.randint(1000, 100000)

# Funktsioon avaliku ja privaatse võtme genereerimiseks
def generate_keys():
    p = generate_large_prime()
    q = generate_large_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

# Funktsioon teksti krüpteerimiseks
def encrypt(message, private_key):
    e, n = private_key

    return [pow(ord(char), e, n) for char in message]

# Funktsioon teksti dekrüpteerimiseks
def decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted_chars = [pow(char, d, n) for char in ciphertext]
    print("Dekrüpteeritud täisarvud:", decrypted_chars)
    decrypted_message = ''.join([chr(char % 256) for char in decrypted_chars])
    return decrypted_message

# Salvestab võtmed failidesse
def save_keys(public_key, private_key):
    with open('avalik_võti.txt', 'w') as file:
        file.write(','.join(map(str, public_key)))
    with open('privaatne_võti.txt', 'w') as file:
        file.write(','.join(map(str, private_key)))

# Laeb võtmed failidest
def load_keys():
    with open('avalik_võti.txt', 'r') as file:
        public_key = tuple(map(int, file.readline().split(',')))
    with open('privaatne_võti.txt', 'r') as file:
        private_key = tuple(map(int, file.readline().split(',')))
    return public_key, private_key

# Peaprogramm
def main():
    print("1. Genereeri RSA võtmed")
    print("2. Krüpteeri tekst")
    print("3. Dekrüpteeri tekst")
    choice = int(input("Vali tegevus: "))

    if choice == 1:
        public_key, private_key = generate_keys()
        save_keys(public_key, private_key)
        print("Võtmed on genereeritud ja salvestatud failidesse.")
    elif choice == 2:
        _, private_key = load_keys()
        message = input("Sisestage tekst, mida soovite krüpteerida: ")
        encrypted_message = encrypt(message, private_key)
        print("Krüpteeritud tekst:", encrypted_message)
    elif choice == 3:
        _, private_key = load_keys()
        ciphertext = eval(input("Sisestage krüpteeritud tekst (kujul [num1, num2, ...]): "))
        decrypted_message = decrypt(ciphertext, private_key)
        print("Dekrüpteeritud tekst:", decrypted_message)
    else:
        print("Vale valik!")

if __name__ == "__main__":
    main()
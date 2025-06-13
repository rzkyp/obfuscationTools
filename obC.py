import base64
import zlib
import os

def obfuscate_code(code: str) -> str:
    compressed = zlib.compress(zlib.compress(code.encode()))
    encoded = base64.b64encode(compressed).decode()
    reversed_encoded = encoded[::-1]
    return reversed_encoded

def deobfuscate_code(encoded: str) -> str:
    try:
        reversed_encoded = encoded[::-1]
        decoded = base64.b64decode(reversed_encoded)
        decompressed = zlib.decompress(zlib.decompress(decoded)).decode()
        return decompressed
    except Exception as e:
        return f"[!] Gagal deobfuscate: {e}"

def output_c_version(obf: str) -> str:
    return f'''
// === C VERSION ===
#include <stdio.h>

int main() {{
    const char *obfuscated_code = "{obf}";
    printf("Obfuscated C code:\\n%%s\\n", obfuscated_code);
    return 0;
}}
'''.strip()

def output_cpp_version(obf: str) -> str:
    return f'''
// === C++ VERSION ===
#include <iostream>
#include <string>

int main() {{
    std::string obfuscated_code = "{obf}";
    std::cout << "Obfuscated C++ code:\\n" << obfuscated_code << std::endl;
    return 0;
}}
'''.strip()

def menu():
    while True:
        print("\n===== MENU OBFUSCATOR C/C++ =====")
        print("1. Encode (Obfuscate) Program C/C++")
        print("2. Decode dari String Obfuscated")
        print("3. Keluar")
        pilih = input("Pilih opsi: ")

        if pilih == "1":
            path = input("Masukkan path file kode C/C++: ").strip()
            if not os.path.exists(path):
                print("[!] File tidak ditemukan.")
                continue

            with open(path, 'r') as f:
                kode = f.read()

            hasil = obfuscate_code(kode)
            print("\n--- Obfuscated String ---\n")
            print(hasil)

            print("\n--- Versi Kode C ---\n")
            print(output_c_version(hasil))
            print("\n--- Versi Kode C++ ---\n")
            print(output_cpp_version(hasil))

        elif pilih == "2":
            print("\nMasukkan string hasil obfuscation:")
            encoded = input(">> ").strip()
            hasil = deobfuscate_code(encoded)
            print("\n--- Hasil Decode ---\n")
            print(hasil)

        elif pilih == "3":
            print("Keluar dari program.")
            break
        else:
            print("Opsi tidak valid.")

if __name__ == "__main__":
    menu()

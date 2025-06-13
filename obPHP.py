import base64
import zlib
import sys

def encode_php_code():
    print("Masukkan kode PHP (tanpa <?php). Akhiri dengan CTRL+Z (Windows) / CTRL+D (Linux/macOS) Lalu Enter :\n")
    php_code = sys.stdin.read()
    data = php_code.encode()

    # 1. Compress dengan zlib (untuk gzuncompress) → 2x
    for _ in range(2):
        data = zlib.compress(data)

    # 2. Compress dengan raw deflate (untuk gzinflate) → 3x
    for _ in range(3):
        data = zlib.compress(data, level=9)[2:-4]

    # 3. Base64 + strrev
    encoded = base64.b64encode(data).decode()[::-1]

    print("\tProgram Sederhana")
    print("\n======= HASIL ENCOD =======\n")
    print(f'$_0xZer0r = "{encoded}";')
    print('eval("?>".gzuncompress(gzuncompress(gzinflate(gzinflate(gzinflate(base64_decode(strrev($_0xZer0r))))))));')


def decode_arif():
    encoded = input("Masukkan isi variabel $_0xZer0r:\n")[::-1]  

    try:
        data = base64.b64decode(encoded)
    except Exception as e:
        print("[!] Gagal decode base64:", e)
        return

    # multi-layer decompress
    def multi_decompress(data, max_layers=10):
        current = data
        for _ in range(max_layers):
            for wbits in (15, -15, 16+15):  # zlib, raw, gzip
                try:
                    current = zlib.decompress(current, wbits)
                    break
                except:
                    continue
            else:
                break
        return current

    try:
        final = multi_decompress(data).decode(errors="replace")
        print("\n======= HASIL DECOD =======\n")
        print(final)
    except Exception as e:
        print("[!] Gagal decode:", e)

def show_license():
    print("""
\tAlat Encode/Decode Eval Obfuscation PHP
\t\tBy 0xZer0r  ~ Insider
""")

def menu():
    while True:
        print("\n====== MENU ======")
        print("1. Encode PHP")
        print("2. Decode to PHP")
        print("3. Lihat License")
        print("0. Keluar")
        pilih = input("Pilih opsi: ")
        if pilih == "1":
            encode_php_code()
        elif pilih == "2":
            decode_arif()
        elif pilih == "3":
            show_license()
        elif pilih == "0":
            break
        else:
            print("Opsi tidak dikenal.")

if __name__ == "__main__":
    menu()

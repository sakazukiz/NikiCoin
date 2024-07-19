import requests
from colorama import init, Fore, Style

# Inisialisasi colorama
init()

def print_colored(text, color=Fore.WHITE):
    """Mencetak teks dengan warna tertentu."""
    print(color + text + Style.RESET_ALL)

# Membaca user_id dari file session.txt
def get_user_id(filename='session.txt'):
    try:
        with open(filename, 'r') as file:
            user_id = file.read().strip()
        return user_id
    except FileNotFoundError:
        print_colored(f"File {filename} tidak ditemukan.", Fore.RED)
        return None

# Mengambil input untuk coins_count dengan batas maksimal
def get_coins_count():
    AIRDROP_EARN = 1000000
    while True:
        try:
            # Cetak tanda pengenal dan output response
            print_colored(r"""                        
 _   _ _____ _   _______ 
| \ | |_   _| | / |_   _|
|  \| | | | | |/ /  | |  
| . ` | | | |    \  | |  
| |\  |_| |_| |\  \_| |_ 
\_| \_/\___/\_| \_/\___/ 
                          """)
            print_colored("Channel TG: @airdrop_ea", Fore.GREEN)
            print_colored("Github: github.com/sakazukiz", Fore.GREEN)
            print_colored("Info: Jangan asal jual ! Ngotak !!", Fore.GREEN)
            print_colored("===== SC BOT CHEAT NIKI COIN =====", Fore.YELLOW)
            print()  # Baris baru
            coins_count = input(f"Berapa koin yang ingin Anda tambahkan (max {AIRDROP_EARN})? ")
            coins_count = int(coins_count)
            if 0 <= coins_count <= AIRDROP_EARN:
                return coins_count
            else:
                print_colored(f"Input tidak valid. Harap masukkan angka antara 0 dan {AIRDROP_EARN}.", Fore.RED)
        except ValueError:
            print_colored("Input tidak valid. Harap masukkan angka yang benar.", Fore.RED)

def add_coins(user_id):
    # Konfigurasi header dan data
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://nikicoin.work',
        'Referer': 'https://nikicoin.work/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    while True:
        # Ambil input untuk coins_count
        coins_count = get_coins_count()

        data = {
            'user_id': user_id,
            'coins_count': coins_count,
            'energy_count': '0',
        }

        # Kirim permintaan POST
        response = requests.post('https://nikicoin.store/update_coins_and_energy/', headers=headers, data=data)

        # Cetak hasil response
        try:
            response_json = response.json()
            if response_json.get("status") == "success":
                print_colored(f"Berhasil menambah {coins_count} koin", Fore.CYAN)
            else:
                print_colored("Gagal menambah koin", Fore.RED)
        except ValueError:
            print_colored("Error decoding JSON response", Fore.RED)
        
        # Tanya apakah ingin mengulangi
        repeat = input("Apakah Anda ingin mengulangi tambah koin? (ya/tidak): ").strip().lower()
        if repeat != 'ya':
            break

def main():
    # Ambil user_id dari session.txt
    user_id = get_user_id()
    if not user_id:
        return

    # Tambah koin
    add_coins(user_id)

if __name__ == "__main__":
    main()

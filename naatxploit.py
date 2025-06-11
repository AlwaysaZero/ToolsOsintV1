import os
import time
import requests
import platform


#BASE BY SXPLOIT
#PENGEMBANG TOOLS MR.N43TXPLOIT

RESET = "\033[0m"
RED = "\033[31m"
PURPLE = "\033[35m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
GREEN = "\033[32m"
BLUE = "\033[34m"

# Fungsi untuk ambil IP publik
def get_public_ip():
    try:
        return requests.get("https://api.ipify.org").text
    except:
        return "Tidak Diketahui"

# Fungsi untuk ambil informasi device secara otomatis
def get_device_info():
    info = platform.uname()
    return f"{info.system} {info.node} - {info.machine} - {info.processor}"

# Data target (bisa custom)
nomor_target = "+63716628727"
pemilik = "Arby-Hex"
tipe = "Mobile"
tanggal_registrasi = "2025-05-09"
expired = "Tidak Ada Informasi"
ping = "37.9/ms"
operator = "IM3"
negara = "Indonesia"
kota = "DKI Jakarta"

# Fungsi utama
def terminal_output():
    os.system('cls' if os.name == 'nt' else 'clear')
    ip_address = get_public_ip()
    device_info = get_device_info()

    print("➤ .>")
    time.sleep(1)

    print("\n\033[91m* DATABASE RAHASIA TERBONGKAR *\033[0m")
    print("\033[91m========== RESULT ==========\033[0m")
    print("\033[95m")
    print(f"Nomor Target        : {nomor_target}")
    print(f"Pemilik             : {pemilik}")
    print(f"Type                : {tipe}")
    print(f"Tanggal Registrasi  : {tanggal_registrasi}")
    print(f"Expired             : {expired}")
    print(f"IP Address          : {ip_address}")
    print(f"Ping                : {ping}")
    print(f"Jenis Operator      : {operator}")
    print(f"Negara              : {negara}")
    print(f"Kota                : {kota}")
    print(f"Device              : {device_info}")
    print("\033[0m")

    print("\033[92m\n✔ Data berhasil diproses. Gunakan dengan bijak.\033[0m\n")
    print("\033[94mroot@localhost:~#\033[0m ", end="")

# Jalankan
terminal_output()



def main():
    os.system("clear")

    print(
    "\033[31m"
    "⠀⠀⠀⠀⠀⠀⠀⠀ ⣀⡤⠔⠒⠊⠉⠉⠉⠉⠙⠒⠲⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⣠⠔⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⣠⠞⠁⠀⣀⠀⠀⠀⠀⢀⣀⡀⠀⢀⣀⠀⠀⠀⠀⢀⠀⠈⠱⣄⠀⠀⠀\n"
    "⠀⠀⠀⡴⠁⡠⣴⠟⠁⢀⠤⠂⡠⠊⡰⠁⠇⢃⠁⠊⠑⠠⡀⠀⢹⣶⢤⡈⢣⡀⠀\n"
    "⠀⠀⡼⢡⣾⢓⡵⠃⡐⠁⠀⡜⠀⠐⠃⣖⣲⡄⠀⠀⠱⠀⠈⠢⠈⢮⣃⣷⢄⢳⠀\n"
    "⠀⢰⠃⣿⡹⣫⠃⡌⠀⠄⠈⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠣⠀⠀⠱⠈⣯⡻⣼⠈⡇\n"
    "⠀⡞⢈⢿⡾⡃⠰⠀⠀⠀⠀⠀⠀⠀⠀⣘⣋⠀⠀⠀⠀⠀⠀⠀⠀⠇⢸⢿⣿⢠⢸\n"
    "⠀⡇⢸⡜⣴⠃⠀⠀⠀⠀⠀⣀⣀⣤⡎⠹⡏⢹⣦⣀⣀⠀⠀⠀⠀⢈⠘⣧⢣⡟⢸\n"
    "⠀⢧⢊⢳⡏⣤⠸⠀⠀⠀⢸⣿⣿⣿⡇⢰⡇⢠⣿⣿⣿⣷⠀⠀⠀⡆⢸⢹⡼⣱⢸\n"
    "⠀⢸⡘⢷⣅⣿⢂⢃⠐⠂⣿⣿⣿⣿⣿⣼⣇⣾⣿⣿⣿⣿⠁⠂⡰⡠⣿⢨⡾⠃⡇\n"
    "⠀⠀⢳⡱⣝⠻⡼⣆⡁⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠐⣰⣇⠿⣋⠝⡼⠀\n"
    "⠀⠀⠀⢳⡈⢻⠶⣿⣞⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢣⣿⡶⠟⢉⡼⠁⠀\n"
    "⠀⠀⠀⠀⠙⢦⡑⠲⠶⠾⠿⢟⣿⣿⣿⣿⣿⣿⣿⣿⡛⠿⠷⠶⠶⠊⡡⠋⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⠙⠦⣝⠛⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⡛⠛⠛⣋⠴⠋⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠦⠿⣿⣿⣿⣿⣿⣿⠿⠧⠒⠋⠁\n"
    "\033[31m"
)
    print(RED + "[ + ] TOOLS OSINT BY ./MR N43TXPLOIT [ + ]" + RESET) 
    print(RED + "This isn’t hacking." + RESET)
    print(RED + "This is observation." + RESET)  
    print(RED + "This is OSINT." + RESET)
    print(RED + "And I’ve been watching you…" + RESET)
    print(RED + "long before you even noticed me." + RESET)
    print(RED + "─ ./MR N43TXPLOIT BLACK HAT" + RESET)     
                                                                                         
    print(RED + "[ + ] C O D E D B Y N A A T X P L O I T " + RESET)
    print(BLUE + "Author : Mr.N43TXPLOIT" + RESET)
    print(BLUE + "Telegram : t.me/natcrazy" + RESET)
    print(BLUE + "Pengembang : Mr.N43TXPLOIT" + RESET)
    print(BLUE + "YouTube : @NatnewEra" + RESET) 
    print(GREEN + "Github : https://github.com/SXploit01" + RESET)

    nik = input(RED + "[ + ] INPUT THE NIK: " + RESET)

    if not nik.isdigit() or len(nik) != 16:
        print(RED + "ERROR! NIK Tidak Valid!" + RESET)
        return

    tanggal = nik[6:8]
    bulan = nik[8:10]
    tahun = nik[10:12]
    provinsi = nik[0:2]
    kabkot = nik[0:4]
    kecamatan = nik[0:6]
    uniqcode = nik[12:16]

    cekjk = int(nik[6:8])
    jeniskelamin = "LAKI-LAKI" if cekjk <= 40 else "WANITA"

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        print(RED + "! Data Tidak Valid !" + RESET)
        return

    provinsi = data.get("provinsi", {}).get(provinsi, provinsi)
    kabkot = data.get("kabkot", {}).get(kabkot, kabkot)
    kecamatan_data = data.get("kecamatan", {}).get(kecamatan, kecamatan)

    if isinstance(kecamatan_data, str):
        kecamatan_name, kode_pos = kecamatan_data.split("--")
    else:
        kecamatan_name, kode_pos = kecamatan, "N/A"

    print(f"{RED}=====OSINT BY ./MR.N43TXPLOIT=====") 
    print(f"{GREEN}TanggalLahir: {tanggal}/{bulan}/{tahun}{RESET}")
    print(f"{GREEN}Kelamin: {jeniskelamin}{RESET}")
    print(f"{GREEN}Provinsi: {provinsi}{RESET}")
    print(f"{GREEN}Regency/City: {kabkot}{RESET}")
    print(f"{GREEN}Kecamatan: {kecamatan_name}{RESET}")
    print(f"{GREEN}KodePos: {kode_pos}{RESET}")
    print(f"{GREEN}KodeUnik: {uniqcode}{RESET}")

if __name__ == "__main__":
    main()

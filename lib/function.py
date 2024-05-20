from lib.package import *
from lib.variable import *

def cetak(*args):
    print(*args)

def fcetak(file, *args):
    with open(file.name, 'a') as f:
        print(*args, file=f)

def sistem(command):
    return os.system(command)

def pergi_ke(label):
    return goto(label)

def Tidur(duration):
    time.sleep(duration)

def keluar():
    pid = os.getpid()
    os.killpg(pid, signal.SIGTSTP)

def noticeDefault():
    with open("error.txt", "a") as file:
        file.write("[ERROR] Kesalahan Saat Menginput Pada Menu\n")
        fcetak(file, "Masukkan Dengan Benar\n")
    cetak("\tSilahkan Coba Lagi.\n")
    input("Press Enter to continue...\n")
    sistem("clear")

def noticeExit():
    sistem("clear")
    waktuDanTanggal()
    cetak("Terima Kasih Telah Menggunakan Aplikasi Beta Sudah Dekat >_<")
    keluar()

def gerakGaris():
    garis = 100
    while garis > 0:
        print("=", end="")
        garis -= 1

def waktuDanTanggal():
    waktu = time.localtime()
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    tanggal = waktu.tm_mday
    indeks_bulan = waktu.tm_mon
    tahun = waktu.tm_year
    jam = waktu.tm_hour
    menit = waktu.tm_min
    detik = waktu.tm_sec
    nama_hari = hari[waktu.tm_wday]
    nama_bulan = bulan[indeks_bulan]
    cetak("Tanggal dan Waktu : %s, %02d %s %04d %02d:%02d:%02d\n" % (nama_hari, tanggal, nama_bulan, tahun, jam, menit, detik))

def alokasiMemoriUrutanPemutaran():
    global urutan_pemutaran
    urutan_pemutaran = [i for i in range(jumlah_lagu)]

def inisialisasiUrutanPemutaran():
    random.shuffle(urutan_pemutaran)

def playMusik():
    pygame.mixer.init()
    pemutaran_selesai = 0
    while True:
        lagu_saat_ini = urutan_pemutaran[pemutaran_selesai]
        if lagu_saat_ini == 0:
            pygame.mixer.music.load("lagu/rapsodi.wav")
        elif lagu_saat_ini == 1:
            pygame.mixer.music.load("lagu/seventeen.wav")
        elif lagu_saat_ini == 2:
            pygame.mixer.music.load("lagu/tokyo_drift.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        pemutaran_selesai += 1
        if pemutaran_selesai == jumlah_lagu:
            inisialisasiUrutanPemutaran()
            pemutaran_selesai = 0

def sistemPlay():
    random.seed(time.time())
    alokasiMemoriUrutanPemutaran()
    inisialisasiUrutanPemutaran()
    playMusik()

def stopPemutaranLagu():
    pygame.mixer.music.stop()

def playPemutaranLagu():
    global current_song_thread
    current_song_thread = threading.Thread(target=sistemPlay)
    current_song_thread.start()

def sistemMusik():
    while True:
        sistem("clear")
        gerakGaris()
        cetak("\n\t\t\t\t\tProgram Playlist Lagu (Musik)")
        gerakGaris()
        cetak("\n\t1. JKT48 - Rapsodi")
        cetak("\t2. JKT48 - Seventeen")
        cetak("\t3. Tokyo Drift - Teriyaki Boyz")
        cetak("\t4. Kembali Ke Awal\n")
        pilihan = input("Masukkan Pilihan Menu Sesuai Nomor Menu Atau Tulis Nama Menunya : ").lower()
        if pilihan == "1" or pilihan == "jkt48 - rapsodi":
            stopPemutaranLagu()
            pygame.mixer.music.load("lagu/rapsodi.wav")
            pygame.mixer.music.play(loops=-1)
            sistemMenu()
        elif pilihan == "2" or pilihan == "jkt48 - seventeen":
            stopPemutaranLagu()
            pygame.mixer.music.load("lagu/seventeen.wav")
            pygame.mixer.music.play(loops=-1)
            sistemMenu()
        elif pilihan == "3" or pilihan == "tokyo drift - teriyaki boyz":
            stopPemutaranLagu()
            pygame.mixer.music.load("lagu/tokyo_drift.wav")
            pygame.mixer.music.play(loops=-1)
            sistemMenu()
        elif pilihan == "4" or pilihan == "kembali ke awal":
            sistemMenu()
        else:
            noticeDefault()

def sistemLogin():
    cetak("\n")
    attempts = 0
    login = 0
    maxAttempts = 3
    loginmax = 3
    username = ""
    password = ""
    inputUsername = ""
    inputPassword = ""
    folder_path = "../coba-coba"

    try:
        with open("data.txt", "r") as dataFile:
            lines = dataFile.readlines()
            if len(lines) < 2:
                cetak("\n\tWelcome, ")
                return
            username = lines[0].strip().split(" : ")[1]
            password = lines[1].strip().split(" : ")[1]
    except FileNotFoundError:
        cetak("\n\tWelcome, ")
        return

    try:
        with open("login.txt", "r") as logFile:
            login = int(logFile.readline().strip().split(" : ")[1])
    except FileNotFoundError:
        pass

    if login >= loginmax:
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            try:
                shutil.rmtree(folder_path)
                cetak("\tAnda telah melebihi batas percobaan untuk login jadi dibanned dan Folder script akan terhapus secara otomatis.\n\tProgram akan keluar~\n\n")
            except Exception as e:
                cetak(f"Gagal menghapus folder '{folder_path}': {e}")
        else:
            cetak(f"Folder '{folder_path}' tidak ditemukan atau bukan direktori.")
        exit(0)

    while attempts < maxAttempts:
        while True:
            inputUsername = input("\tMasukkan username : ").strip()
            if inputUsername:
                break

        while True:
            inputPassword = getpass.getpass("\tMasukkan password : ")
            if inputPassword:
                break

        if inputUsername == username and inputPassword == password:
            cetak("\n\t[Login sukses] Selamat datang, {}\n\t".format(username))
            try:
                os.remove("login.txt")
            except FileNotFoundError:
                pass
            break
        else:
            attempts += 1
            if maxAttempts - attempts != 0:
                cetak("\n\t[Login gagal] Sisa percobaan : {}\n".format(maxAttempts - attempts))
            else:
                cetak("\n\t[Login gagal] Sisa percobaan telah habis\n")

    if attempts == maxAttempts:
        login += 1
        with open("login.txt", "w") as logFile:
            logFile.write("[ERROR] Gagal Login : {}".format(login))
        cetak("\tAnda telah melebihi batas percobaan.\n\tProgram akan keluar~\n\n")
        exit(0)

def sistemPembuka():
    sistem("clear")
    cetak("\t\t\t[ Sekedar coba-coba ]\n\t")
    gerakGaris()
    cetak("\n\tNama\t : Rivai")
    cetak("\tNIM\t : 20230801290\t")
    gerakGaris()
    sistemLogin();
    playPemutaranLagu()
    input("\nPress Enter to continue...")
    if threadCreationStatus == 0:
        sistemMenu()

def sistemMenu():
    sistem("clear")
    gerakGaris()
    cetak("\n\t\t\t\tAplikasi Beta Sudah Dekat V4\t")
    gerakGaris()
    cetak("\n\t1. Ganti Lagu")
    cetak("\t2. Keluar Aplikasi\n")
    pilihan_menu = input("\tMasukkan Pilihan Menu Sesuai Nomor Menu Atau Tulis Nama Menunya : ").lower()
    if pilihan_menu in ["1", "ganti lagu"]:
        sistemMusik()
    elif pilihan_menu in ["2", "keluar aplikasi"]:
        noticeExit()
    else:
        noticeDefault()
        sistemMenu()

def sistemSubMenu():
    gerakGaris()
    cetak("\n\t\t\t\t\t\t   Pilihan Menu\t")
    gerakGaris()
    cetak("\t1. Kembali Ke Awal")
    cetak("\t2. Keluar Aplikasi\n")
    pilihan_submenu = input("\tMasukkan Pilihan Menu Sesuai Nomor Menu Atau Tulis Nama Menunya : ").lower()
    if pilihan_submenu in ["1", "kembali ke awal"]:
        sistemMenu()
    elif pilihan_submenu in ["2", "keluar aplikasi"]:
        noticeExit()
    else:
        noticeDefault()
        sistemSubMenu()

def sistemInti():
    sistemPembuka()
    if threadCreationStatus == 0:
        sistemMenu()
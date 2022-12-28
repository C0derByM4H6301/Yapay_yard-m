import subprocess

def check_if_running(process_name):
    # Sistemde çalışan tüm işlemleri listeleyen bir komut çalıştırıyoruz
    cmd = "tasklist"
    # Bu komutun çıktısını alıyoruz
    output = subprocess.check_output(cmd)
    # Çıktıyı bir dize olarak okuyoruz
    output_str = output.decode("utf-8")
    # Çıktıda aradığımız işlem adını arıyoruz
    if process_name in output_str:
        # Eğer işlem adı çıktıda mevcutsa, işlem çalışıyor
        return True
    else:
        # Eğer işlem adı çıktıda yoksa, işlem çalışmıyor
        return False

# Örnek olarak, Counter-Strike oyununun çalışıp çalışmadığını kontrol ediyoruz
if check_if_running("csgo.exe"):
    # Eğer oyun çalışıyorsa, oyunu durduruyoruz
    subprocess.run(["taskkill", "/f", "/im", "csgo.exe"])
    print("Counter-Strike durduruldu")
else:
    # Eğer oyun zaten durdurulmuşsa, bir mesaj yazdırıyoruz
    print("Counter-Strike zaten durdurulmuş")

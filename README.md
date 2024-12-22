# Python Servisi Oluşturma

Bu proje, belirlenen bir dizini izleyerek dosya sistemindeki değişiklikleri (oluşturma, silme, değiştirme) tespit eden ve bu değişiklikleri JSON formatında bir log dosyasına kaydeden bir Python servisidir. Servis, Linux ortamında çalışır ve `systemd` kullanılarak bir sistem servisi olarak yapılandırılmıştır.

## Projenin Özellikleri

- **Dizin İzleme**: Belirtilen dizindeki tüm değişiklikleri (dosya/dizin ekleme, silme, değiştirme) gerçek zamanlı olarak tespit eder.
- **Loglama**: Tespit edilen değişiklikleri JSON formatında bir log dosyasına kaydeder.
- **Linux Sistem Servisi**: Proje, Linux ortamında bir `systemd` servisi olarak çalışır. Sistem yeniden başlatıldığında servis otomatik olarak başlar.

## Kurulum

1. **Gerekli Kütüphaneleri Yükleyin**:
   ```bash
   pip install watchdog
2. **Dizin Yapısını Oluşturun, İzlenecek dizin ve log dosyalarının bulunacağı dizini oluşturun**
   ```bash
   mkdir -p /home/ubuntu/bsm/test
   mkdir -p /home/ubuntu/bsm/logs
3. **Python Scriptini Çalıştırın, Scripti manuel olarak test etmek için:**
      ```bash
      python3 directory_watcher.py
4. **Servisi Etkinleştirin, Servis dosyasını oluşturduktan sonra:**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable directory_watcher.service
   sudo systemctl start directory_watcher.service

## Kullanım

1. **Servis Başlatma:**
   ```bash
   sudo systemctl start directory_watcher.service
2. **Log Dosyasını Kontrol Etme:**
   İzlenen dizindeki değişiklikler /home/ubuntu/bsm/logs/changes.json dosyasına kaydedilir.
      ```bash
      cat /home/ubuntu/bsm/logs/changes.json
3. **Servisi Durduma:**      
   ```bash
   sudo systemctl stop directory_watcher.service

## Yapılanlar
- **Python Scripti**: İzleme ve loglama işlemleri için watchdog kütüphanesi kullanılarak bir script yazıldı.
- **Loglama**: JSON formatında loglama işlemi gerçekleştirildi.
- **Linux Sistem Servisi**: Script bir systemd servisi olarak yapılandırıldı ve otomatik başlatma ayarlandı.
- **GitHub ve Video**: Proje GitHub’a yüklendi ve bir video çekilerek YouTube’a yüklendi.

## Gereksinimler
- **Python 3.8 veya Daha Üstü**
- **Linux İşletim Sistemi**
- `watchdog` **Kütüphanesi**

## Proje Linkleri
- **YouTube Videosu**:
  
   

   

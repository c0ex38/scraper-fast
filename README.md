<div align="center">

# 🔥 Firecrawl FastAPI Wrapper

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Firecrawl-FF6B35?style=for-the-badge&logo=fire&logoColor=white" alt="Firecrawl">
</p>

<p align="center">
  <strong>Web sayfalarını anında Markdown ve HTML formatına dönüştürün!</strong>
</p>

<p align="center">
  Modern, hızlı ve kullanıcı dostu bir web scraping aracı.
</p>

</div>

---

## ✨ Özellikler

- 🎨 **Modern UI/UX** - Animasyonlu, gradient efektli ve glassmorphism tasarım
- 📝 **Markdown Dönüşümü** - Web sayfalarını temiz markdown formatına çevir
- 🌐 **HTML Önizleme** - İçeriği iframe'de canlı görüntüle
- 📋 **Tek Tık Kopyalama** - Sonuçları kolayca panoya kopyala
- ⚡ **Hızlı Performans** - Saniyeler içinde sonuç al
- 🔄 **Real-time Feedback** - Loading ve başarı durumu göstergeleri
- � **API Endpoints** - Programatik erişim için RESTful API
- 🛡️ **Hata Yönetimi** - Kullanıcı dostu hata mesajları

## 🚀 Hızlı Başlangıç

### Gereksinimler

- Python 3.8+
- Firecrawl API anahtarı ([buradan](https://firecrawl.dev) alabilirsiniz)

### Kurulum

1️⃣ **Projeyi klonlayın**

```bash
git clone https://github.com/c0ex38/firecrawl-fastapi-wrapper.git
cd firecrawl-fastapi-wrapper
```

2️⃣ **Sanal ortam oluşturun**

```bash
# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

3️⃣ **Bağımlılıkları yükleyin**

```bash
pip install -r requirements.txt
```

4️⃣ **Ortam değişkenlerini ayarlayın**

`.env` dosyası oluşturun ve API anahtarınızı ekleyin:

```env
API_KEY="fc-YOUR_API_KEY_HERE"
```

5️⃣ **Uygulamayı başlatın**

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

🎉 **Tamamdır!** Tarayıcınızda [http://localhost:8000](http://localhost:8000) adresine gidin.

---

## 📖 Kullanım

### Web Arayüzü

1. Ana sayfada scrape etmek istediğiniz URL'i girin
2. 🚀 **Scrape Et** butonuna tıklayın
3. Sonuçları **Markdown** veya **HTML Önizleme** sekmelerinde görüntüleyin
4. İstediğiniz içeriği **📋 Kopyala** butonu ile panoya kopyalayın

### API Endpoints

#### 🔹 Tek Sayfa Scraping

```bash
curl "http://localhost:8000/scrape?url=https://example.com"
```

**Yanıt:**
```json
{
  "markdown": "# Sayfa içeriği...",
  "html": "<html>...</html>",
  "metadata": {...}
}
```

#### 🔹 Site Crawling

```bash
curl "http://localhost:8000/crawl?url=https://example.com&limit=10"
```

## 🛠️ Teknolojiler

- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, hızlı Python web framework
- **[Firecrawl](https://firecrawl.dev)** - Güçlü web scraping API
- **[Uvicorn](https://www.uvicorn.org/)** - ASGI server
- **[Python Dotenv](https://github.com/theskumar/python-dotenv)** - Ortam değişkenleri yönetimi

---

## 📁 Proje Yapısı

```
firecrawl-fastapi-wrapper/
├── main.py              # Ana uygulama dosyası
├── requirements.txt     # Python bağımlılıkları
├── .env                 # Ortam değişkenleri (git'e eklenmez)
├── .gitignore          # Git ignore kuralları
└── README.md           # Proje dokümantasyonu
```

---

## ⚙️ Yapılandırma

`.env` dosyanızda aşağıdaki değişkenleri ayarlayabilirsiniz:

```env
API_KEY="fc-YOUR_API_KEY_HERE"  # Firecrawl API anahtarınız
```

---

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

---


<div align="center">

**[⬆ Başa Dön](#-firecrawl-fastapi-wrapper)**

</div>

# FastAPI CRUD dengan Firebase Firestore (OOP Sederhana)

API REST sederhana menggunakan FastAPI dan Firebase Firestore dengan penerapan konsep Object-Oriented Programming (OOP).

## Konsep OOP yang Digunakan

### 1. Enkapsulasi

- Menyembunyikan detail implementasi dalam kelas
- Menggunakan metode publik untuk mengakses fungsionalitas kelas
- Menyediakan interface yang bersih untuk pengguna kelas

### 2. Abstraksi

- Menyediakan interface sederhana untuk operasi kompleks
- Memisahkan logika bisnis (Service) dari akses data (Repository)

### 3. Pola Desain

- **Repository Pattern**: Memisahkan logika akses data dari logika bisnis
- **Service Pattern**: Menangani logika bisnis dan validasi
- **Singleton Pattern**: Memastikan hanya ada satu instance database di seluruh aplikasi

## Struktur Proyek

```
fastapi-firebase-crud/
├── app/
│   ├── __init__.py        # File inisialisasi
│   ├── main.py            # File utama aplikasi
│   ├── database.py        # Koneksi database (Firebase)
│   ├── models.py          # Model data (Pydantic)
│   ├── repository.py      # Akses database
│   ├── service.py         # Logika bisnis
│   ├── router.py          # API routes
├── requirements.txt       # Dependensi proyek
└── README.md              # Dokumentasi
```

## Fitur

- CRUD (Create, Read, Update, Delete) operasi untuk data pengguna
- Validasi data dengan Pydantic
- Dokumentasi otomatis dengan Swagger UI
- Integrasi dengan Firebase Firestore sebagai database
- Penerapan konsep OOP yang sederhana dan mudah dipahami

## Menjalankan Aplikasi

1. Clone repository ini

```bash
git clone https://github.com/username/fastapi-firebase-crud.git](https://github.com/MhdIqbalPratama/simpleCRUDAPI-FastAPI.git
cd simpleCRUDAPI-FastAPI
```

2. Buat dan aktifkan virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Untuk Linux/Mac
venv\Scripts\activate     # Untuk Windows
```

3. Install dependensi

```bash
pip install -r requirements.txt
```

4. Setup Firebase Firestore

   - Buat project baru di [Firebase Console](https://console.firebase.google.com/)
   - Di Project Settings > Service Accounts, generate kunci private baru (JSON)
   - Simpan file JSON tersebut di folder project
   - Update path di file `app/database.py`

5. Jalankan aplikasi

```bash
python -m "file_path"
```

## Menggunakan API

- Dokumentasi API: http://localhost:8000/docs
- OpenAPI Schema: http://localhost:8000/openapi.json

### Endpoint API

- `POST /users/` - Membuat pengguna baru
- `GET /users/` - Mendapatkan semua pengguna
- `GET /users/{user_id}` - Mendapatkan pengguna berdasarkan ID
- `PUT /users/{user_id}` - Memperbarui pengguna berdasarkan ID
- `DELETE /users/{user_id}` - Menghapus pengguna berdasarkan ID

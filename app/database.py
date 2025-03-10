import firebase_admin
from firebase_admin import credentials, firestore
import os

# Singleton pattern untuk Firebase client
class FirebaseClient:
    """
    Kelas singleton untuk Firebase client.
    Memastikan hanya ada satu instance Firebase client di seluruh aplikasi.
    """
    _instance = None
    _db = None
    
    @classmethod
    def get_instance(cls):
        """Mendapatkan instance singleton dari FirebaseClient"""
        if cls._instance is None:
            cls._instance = FirebaseClient()
        return cls._instance
    
    def get_db(self):
        """Mendapatkan instance Firestore database"""
        if self._db is None:
            self._db = firestore.client()
        return self._db

def initialize_firebase():
    """
    Inisialisasi Firebase Admin SDK jika belum diinisialisasi.
    
    Returns:
        Firestore client untuk akses database
    """
    
    print("Starting Firebase initialization...")
    # Use the correct file path
    cred_path = os.environ.get("db_path")
    # cred_path = os.environ.get("FIREBASE_CREDENTIALS_PATH", 
        # "C:\\Users\\LENOVO\\Documents\\Iqbal\\simpleCRUDFastAPI\\simplecrudfastapi-firebase-adminsdk-fbsvc-4393ab9fae.json")
    
    print(f"Using credentials path: {cred_path}")
    print(f"File exists: {os.path.exists(cred_path)}")
    # Make sure credentials path is correctly specified
    if not firebase_admin._apps:
        # Gunakan variabel lingkungan atau file lokal
        # cred_path = os.environ.get("FIREBASE_CREDENTIALS_PATH", r"C:\Users\LENOVO\Documents\Iqbal\simpleCRUDFastAPI\simplecrudfastapi-firebase-adminsdk-fbsvc-666d6c081f.json")
        # cred_path = os.environ.get("FIREBASE_CREDENTIALS_PATH", "C:\\Users\\LENOVO\\Documents\\Iqbal\\simpleCRUDFastAPI\\simplecrudfastapi-firebase-adminsdk-fbsvc-666d6c081f.json")
        
        # Inisialisasi Firebase app
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
    
    # Kembalikan client untuk Firestore
    return FirebaseClient.get_instance().get_db()

def get_db():
    """
    Dapatkan instance database Firestore.
    
    Returns:
        Firestore client
    """
    return FirebaseClient.get_instance().get_db()
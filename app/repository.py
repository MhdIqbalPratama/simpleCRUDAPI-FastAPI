from datetime import datetime
from typing import List, Dict, Any, Optional

from database import get_db
from models import UserCreate, UserUpdate

class UserRepository:
    """
    Kelas repository untuk operasi data pengguna dengan Firestore.
    Mengimplementasikan pola Repository untuk mengakses database.
    """
    
    def __init__(self):
        """Inisialisasi repository dengan database dan collection"""
        self.db = get_db()
        self.collection = self.db.collection('users')
    
    async def create(self, user_data: UserCreate) -> Dict[str, Any]:
        """
        Membuat pengguna baru di Firestore
        
        Args:
            user_data: Data pengguna yang akan dibuat
            
        Returns:
            Data pengguna yang dibuat termasuk ID
        """
        now = datetime.utcnow()
        
        # Konversi model Pydantic ke dict dan tambahkan timestamp
        user_dict = user_data.dict()
        user_dict.update({
            'created_at': now,
            'updated_at': now
        })
        
        # Tambahkan ke Firestore
        new_user_ref = self.collection.document()
        new_user_ref.set(user_dict)
        
        # Kembalikan data pengguna yang dibuat dengan ID
        created_user = user_dict.copy()
        created_user['id'] = new_user_ref.id
        
        return created_user
    
    async def get_all(self) -> List[Dict[str, Any]]:
        """
        Mendapatkan semua pengguna dari Firestore
        
        Returns:
            List data pengguna
        """
        users = []
        for doc in self.collection.stream():
            user_data = doc.to_dict()
            user_data['id'] = doc.id
            users.append(user_data)
        return users
    
    async def get_by_id(self, user_id: str) -> Optional[Dict[str, Any]]:
        """
        Mendapatkan pengguna berdasarkan ID dari Firestore
        
        Args:
            user_id: ID pengguna
            
        Returns:
            Data pengguna atau None jika tidak ditemukan
        """
        doc = self.collection.document(user_id).get()
        if not doc.exists:
            return None
        
        user_data = doc.to_dict()
        user_data['id'] = doc.id
        return user_data
    
    async def get_by_email(self, email: str) -> List[Dict[str, Any]]:
        """
        Mendapatkan pengguna berdasarkan email dari Firestore
        
        Args:
            email: Email pengguna
            
        Returns:
            List data pengguna (biasanya 0 atau 1)
        """
        query = self.collection.where('email', '==', email).limit(1)
        results = query.get()
        
        users = []
        for doc in results:
            user_data = doc.to_dict()
            user_data['id'] = doc.id
            users.append(user_data)
        
        return users
    
    async def update(self, user_id: str, update_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Memperbarui pengguna di Firestore
        
        Args:
            user_id: ID pengguna
            update_data: Data yang akan diperbarui
            
        Returns:
            Data pengguna yang diperbarui atau None jika tidak ditemukan
        """
        # Tambahkan timestamp pembaruan
        update_data['updated_at'] = datetime.utcnow()
        
        # Update di Firestore
        user_ref = self.collection.document(user_id)
        user_ref.update(update_data)
        
        # Dapatkan dan kembalikan data yang diperbarui
        updated_doc = user_ref.get()
        if not updated_doc.exists:
            return None
            
        updated_user = updated_doc.to_dict()
        updated_user['id'] = user_id
        
        return updated_user
    
    async def delete(self, user_id: str) -> bool:
        """
        Menghapus pengguna dari Firestore
        
        Args:
            user_id: ID pengguna
            
        Returns:
            True jika berhasil dihapus
        """
        self.collection.document(user_id).delete()
        return True
from typing import List, Dict, Any, Optional
from fastapi import HTTPException

from models import UserCreate, UserUpdate
from repository import UserRepository

class UserService:
    """
    Kelas service untuk logika bisnis pengguna.
    Mengimplementasikan pola Service untuk memisahkan logika bisnis dari lapisan presentasi.
    """
    
    def __init__(self):
        """Inisialisasi service dengan repository"""
        self.repository = UserRepository()
    
    async def create_user(self, user: UserCreate) -> Dict[str, Any]:
        """
        Membuat pengguna baru dengan validasi
        
        Args:
            user: Data pengguna yang akan dibuat
            
        Returns:
            Data pengguna yang dibuat
            
        Raises:
            HTTPException: Jika email sudah terdaftar
        """
        # Periksa apakah pengguna dengan email yang sama sudah ada
        existing_users = await self.repository.get_by_email(user.email)
        if existing_users:
            raise HTTPException(
                status_code=400, 
                detail="User dengan email ini sudah terdaftar"
            )
        
        # Buat pengguna
        return await self.repository.create(user)
    
    async def get_users(self) -> List[Dict[str, Any]]:
        """
        Mendapatkan semua pengguna
        
        Returns:
            List data pengguna
        """
        return await self.repository.get_all()
    
    async def get_user(self, user_id: str) -> Dict[str, Any]:
        """
        Mendapatkan pengguna berdasarkan ID dengan penanganan error
        
        Args:
            user_id: ID pengguna
            
        Returns:
            Data pengguna
            
        Raises:
            HTTPException: Jika pengguna tidak ditemukan
        """
        user = await self.repository.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=404, 
                detail=f"User dengan ID {user_id} tidak ditemukan"
            )
        return user
    
    async def update_user(self, user_id: str, user_update: UserUpdate) -> Dict[str, Any]:
        """
        Memperbarui pengguna dengan validasi
        
        Args:
            user_id: ID pengguna
            user_update: Data yang akan diperbarui
            
        Returns:
            Data pengguna yang diperbarui
            
        Raises:
            HTTPException: Jika pengguna tidak ditemukan atau tidak ada data yang diperbarui
        """
        # Pastikan pengguna ada
        await self.get_user(user_id)
        
        # Hanya update field yang disediakan
        update_data = {k: v for k, v in user_update.dict().items() if v is not None}
        
        if not update_data:
            raise HTTPException(
                status_code=400, 
                detail="Tidak ada data yang diperbarui"
            )
        
        # Update pengguna
        updated_user = await self.repository.update(user_id, update_data)
        if not updated_user:
            raise HTTPException(
                status_code=404, 
                detail=f"User dengan ID {user_id} tidak ditemukan"
            )
        
        return updated_user
    
    async def delete_user(self, user_id: str) -> None:
        """
        Menghapus pengguna dengan penanganan error
        
        Args:
            user_id: ID pengguna
            
        Raises:
            HTTPException: Jika pengguna tidak ditemukan
        """
        # Pastikan pengguna ada
        await self.get_user(user_id)
        
        # Hapus pengguna
        await self.repository.delete(user_id)
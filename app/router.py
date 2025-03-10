from fastapi import APIRouter, HTTPException, status

from typing import List

from models import UserCreate, User, UserUpdate
from service import UserService

# Buat router untuk endpoint users
router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "User tidak ditemukan"}},
)

# Buat instance UserService
user_service = UserService()

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """
    Membuat pengguna baru dengan data yang divalidasi
    
    Args:
        user: Data pengguna yang akan dibuat
        
    Returns:
        Data pengguna yang dibuat
    """
    return await user_service.create_user(user)

@router.get("/", response_model=List[User])
async def read_users():
    """
    Mengambil semua pengguna
    
    Returns:
        List data pengguna
    """
    return await user_service.get_users()

@router.get("/{user_id}", response_model=User)
async def read_user(user_id: str):
    """
    Mengambil pengguna berdasarkan ID
    
    Args:
        user_id: ID pengguna
        
    Returns:
        Data pengguna
    """
    return await user_service.get_user(user_id)

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: str, user_update: UserUpdate):
    """
    Memperbarui pengguna berdasarkan ID
    
    Args:
        user_id: ID pengguna
        user_update: Data yang akan diperbarui
        
    Returns:
        Data pengguna yang diperbarui
    """
    return await user_service.update_user(user_id, user_update)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str):
    """
    Menghapus pengguna berdasarkan ID
    
    Args:
        user_id: ID pengguna
    """
    await user_service.delete_user(user_id)
    return None
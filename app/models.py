from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

# Model dasar untuk pengguna
class UserBase(BaseModel):
    """Model dasar untuk data pengguna dengan validasi"""
    name: str = Field(..., min_length=2, max_length=100, description="Nama lengkap pengguna")
    email: EmailStr = Field(..., description="Alamat email pengguna")
    phone: str = Field(..., pattern=r"^\+?[0-9]{10,15}$", description="Nomor telepon pengguna")
    address: Optional[str] = Field(None, description="Alamat pengguna")

# Model untuk membuat pengguna baru
class UserCreate(UserBase):
    """Model untuk membuat pengguna baru"""
    pass

# Model untuk mengupdate pengguna (semua field opsional)
class UserUpdate(BaseModel):
    """Model untuk memperbarui pengguna dengan field opsional"""
    name: Optional[str] = Field(None, min_length=2, max_length=100, description="Nama lengkap pengguna")
    email: Optional[EmailStr] = Field(None, description="Alamat email pengguna")
    phone: Optional[str] = Field(None, pattern=r"^\+?[0-9]{10,15}$", description="Nomor telepon pengguna")
    address: Optional[str] = Field(None, description="Alamat pengguna")

# Model lengkap pengguna untuk respons API
class User(UserBase):
    """Model lengkap pengguna dengan ID dan timestamp"""
    id: str = Field(..., description="ID unik pengguna")
    created_at: datetime = Field(..., description="Tanggal pembuatan")
    updated_at: datetime = Field(..., description="Tanggal pembaruan terakhir")

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
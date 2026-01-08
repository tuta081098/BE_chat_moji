import os
import motor.motor_asyncio
from beanie import init_beanie
from dotenv import load_dotenv # Import thư viện đọc file .env

# Import các models của bạn
from models.users import User
from models.chat import Conversation, Message
from models.friends import FriendRequest

# 1. Load biến môi trường từ file .env (chỉ có tác dụng khi chạy Local)
load_dotenv()

# 2. Lấy URL từ biến môi trường.
# Nếu không tìm thấy (lỡ quên set), nó sẽ fallback về localhost để không crash app
MONGO_URL = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "chat_moji_db"

async def init_db():
    # Tạo client kết nối
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

    database = client[DB_NAME]

    # Khởi tạo Beanie
    await init_beanie(database=database, document_models=[
        User,
        Conversation,
        Message,
        FriendRequest
    ])
import os 
import dotenv

dotenv.load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')
KEY = os.getenv('KEY')
BOT_KEY = os.getenv('BOT_KEY')

# postgresql+asyncpg://postgres:postgres@localhost:5432/sa
# f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
DSN = f"postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
# return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}/{self.DB_PORT}/{self.DB_NAME}"




# Don't Remove Credit Tg - @Tushar0125
# Ask Doubt on telegram @Tushar0125

from os import environ

API_ID = int(environ.get("API_ID", "39683282")) #Replace with your api id
API_HASH = environ.get("API_HASH", "ab1cc41ca283d480ebe386b1dce182f3") #Replace with your api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "8826383680:AAEHUDqDTE1bcqkdiwSYdZBIJHbdwpPDQac") #Replace with your bot token

# Database Configuration for MongoDB
# Example: "mongodb://user:password@host:port/dbname"
# For MongoDB Atlas: "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/<dbname>?retryWrites=true&w=majority"
DATABASE_URL = environ.get("DATABASE_URL")
# Replace "your_bot_db" with your desired database name.
# For local testing, you might use "mongodb://localhost:27017/your_bot_db"

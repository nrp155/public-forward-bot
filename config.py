import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "4608228"))
    API_HASH = os.environ.get("API_HASH", "7d2ccae297d9bddc2c1a704f4db9051a")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6963439535:AAGCg3FSpifxmAxaD7waoQ8dBpxNcdnMN7A")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "1553961614")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://fileforward:fileforward@cluster0.p566uax.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQBGUOQAw8z3Jl48cby0DCOCk-oLZ0soHc-4wPf1Q2XhNq6XQIb4TQ24Wv583dxwAksneN_ARFUWMHegT4PoRkUI3hxVRFJiDcFtSeLgxhK87ayC7EvXOoXYqR5U-oeZa_AGyAFvzhi2RnHzMnvmx47DOZjS92xymL53nu-82GRUTYvsWUWdNjmO4CiuQIXdlohX8SYrJCzz58cAk3hYQU7mCDPrQqhxroSOPMJzoPTZMWl4B_QGmSmmtrhSCy27p9H-piR57oOLFkn5XFs0le24IPXUORyy9vuNT8kOvQnbi-aPANaZWzCrPD6txc1m2_jaerodmJV2h0bMUWVwFVhjqLVtQAAAAAGfDaevAQ")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001390161207"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "https://t.me/subscenelkforward_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

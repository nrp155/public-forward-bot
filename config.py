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
    SESSION = os.environ.get("SESSION", "BQBGUOQAjq7INYXmg5fYTRD77TclGF_inTQzP6flqSd7uJiyLz89RWb9FojDWo5P6TOq3UsbCZQqe2kHvZKjTjGD0CayB45eODHUSdDnhu04fi_NW11I47jBc3Pv8xEwSh31nVtMRP6XZThQTtGzNqpa-63xeq5Qva1OFoZf0ZWWYSRo6D2YcIYRlmlMzm82V_Fu6F80g48KcqZcqygVdgAmqlh6v8r0sV7s1cXp2Qt-lYo6WnEPO7F3T5nsml10M63NXde292H5sDm-L0InFSyQMY_0FljHWUuGfQ54qA_1BfCRkx5A8zRWkNcGNNcpstcqBjCBjz4wWX5Dp0maoP-5SgEEtwAAAABcn5KOAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001390161207"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "https://t.me/subscenelkforward_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

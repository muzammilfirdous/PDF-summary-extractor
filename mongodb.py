from pymongo import MongoClient
import logging

# MongoDB connection setup
client = MongoClient('mongodb+srv://munnumullappilly:vC23E10FxJIsD42D@cluster0.rt8lk.mongodb.net/')
db = client['pdf_pipeline']

def store_pdf_metadata(filename, filepath, filesize):
    """
    Stores PDF metadata in MongoDB.
    """
    try:
        db.pdfs.insert_one({
            'filename': filename,
            'filepath': filepath,
            'filesize': filesize,
            'summary': None,
            'keywords': None
        })
    except Exception as e:
        logging.error(f"Error storing metadata for {filename}: {e}")

def update_pdf_summary(filename, summary, keywords):
    """
    Updates MongoDB record with PDF summary and keywords.
    """
    try:
        db.pdfs.update_one(
            {'filename': filename},
            {'$set': {'summary': summary, 'keywords': keywords}}
        )
    except Exception as e:
        logging.error(f"Error updating summary for {filename}: {e}")

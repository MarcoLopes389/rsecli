from database.database import get_infos_collection

def delete_ips():
    get_infos_collection().delete_many({})
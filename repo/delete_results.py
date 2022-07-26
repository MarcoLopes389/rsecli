from database.database import get_results_collection

def delete_results():
    get_results_collection().delete_many({})
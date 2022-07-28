from database.database import get_results_collection

def get_all_results():
    results = get_results_collection().find()
    return results
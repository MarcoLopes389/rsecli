from database.database import get_results_collection
from tabulate import tabulate

def get_all_results():
    results = get_results_collection().find()
    table = []
    for result in results:
        table.append([result['results'], result['ip'], result['command']])
    print(tabulate(table, headers=['Results', 'IP', 'Command']))
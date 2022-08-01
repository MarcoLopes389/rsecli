from tabulate import tabulate

from repo.get_all_results import get_all_results

def print_results():
    results = get_all_results()
    table = []
    
    for result in results:
        table.append([result['results'], result['ip'], result['command']])

    print(tabulate(table, headers=['Results', 'IP', 'Command']))
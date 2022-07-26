from database.database import get_infos_collection

def print_registred_ips():
    infos = get_infos_collection().find()
    print('Registred IPs:\n')
    for info in infos:
        print(info['name'], '\t', info['ip'])
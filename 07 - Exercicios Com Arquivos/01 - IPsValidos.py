import re

def validar_ip(ip):
    # Define a expressão regular para um endereço IPv4
    padrao_ipv4 = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if padrao_ipv4.match(ip):
        # Verifica se cada parte do IP está entre 0 e 255
        partes = ip.split('.')
        for parte in partes:
            if int(parte) < 0 or int(parte) > 255:
                return False
        return True
    return False

with open('01 - IPsParaValidar.txt', 'r') as arquivo:
    x = arquivo.readlines()


with open('01 - IPsValidos.txt', 'a') as ips:
    
    ips.writelines('--- Ips Validos --- \n')
    for ip in x:
        if validar_ip(ip):
            ips.writelines(ip)

    ips.writelines('\n')
    ips.writelines('--- Ips Invalidos --- \n')

    for ip in x:
        if not validar_ip(ip):
            ips.writelines(ip)
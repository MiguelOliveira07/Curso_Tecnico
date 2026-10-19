import flet as ft
import ipaddress as ip

def ip_host(meu_ip):
    endereco_host = ip.IPv4Address(meu_ip)
    (endereco_host)
    return endereco_host
    
    
def ip_rede(meu_ip):
    endereco_rede = ip.IPv4Network(meu_ip)
    print(endereco_rede) #mostrar enederço de rede
    print(endereco_rede.broadcast_address) # mostrar boradcast
    print(endereco_rede.network_address) #mostrar ip da rede
    print(endereco_rede.with_netmask) # mostrar mascara da rede
    return endereco_rede.network_address
    
    
def verificar_host(host,rede):
    ip_rede(rede)
    ip_host(host)
    if ip.IPv4Address(host) in ip.IPv4Network(rede):
       print('sim')
    else:
        print('Não')
     
    
def main(page: ft.Page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_host.value))
        meu_host = str(new_host.value)
        meu_rede = str(new_rede.value)
        verificar_host(meu_host,meu_rede)    
        new_host.value = ""
        page.update()


    new_host = ft.TextField(hint_text="Entre com um ip de HOST válido:")
    new_rede = ft.TextField(hint_text="Entre com um ip de REDE válido:")

    page.add(new_host, new_rede, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked))

ft.app(main)

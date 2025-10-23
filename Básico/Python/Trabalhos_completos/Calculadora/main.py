import flet as ft
import ipaddress as ip

def ip_host(meu_ip):
    endereco_host = ip.IPv4Address(meu_ip)
    #(endereco_host)
    #print(endereco_host.is_private)
    #print(endereco_host.max_prefixlen)
    #print(endereco_host.version)
    return endereco_host
    
    
def ip_rede(meu_ip):
    endereco_rede = ip.IPv4Network(meu_ip)
    #print(endereco_rede)
    #print(endereco_rede.broadcast_address)
    #print(endereco_rede.network_address)
    #print(endereco_rede.with_netmask)
    return endereco_rede.network_address
    
    
def verificar_host(ip):
    rede = '192.168.15.128/26'
    end_rede = ip_rede(rede)
    end_host = ip_host(ip)
    print(end_rede, end_host)
     
    
def main(page: ft.Page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        verificar_host(new_task.value)    
        new_task.value = ""
        page.update()


    new_task = ft.TextField(hint_text="Entre com um ip válido:")

    page.add(new_task, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked))

ft.app(main)

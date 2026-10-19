import flet as ft
import ipaddress as ip

def ip_host(meu_ip):
    endereco_host = ip.IPv4Address(meu_ip)
    (endereco_host)
    return endereco_host
    
    
def ip_rede(meu_ip):
    endereco_rede = ip.IPv4Network(meu_ip)
    mascara = endereco_rede.with_netmask
    mascara_separada = mascara.split('/')
    
    info = [
        f'O Endereço de rede: {endereco_rede}',
        f'Broadast: {endereco_rede.broadcast_address}',
        f'Ip da rede: {endereco_rede.network_address}',
        f'Mácara da rede: {mascara_separada[1]}'
    ]
    
    return endereco_rede.network_address, info
    
    
def verificar_host(host, rede):
    try:
        rede_address, info = ip_rede(rede)
        ip_host(host)
        if ip.IPv4Address(host) in ip.IPv4Network(rede, strict=False):
            info.append("O host pertence à rede: Sim")
        else:
            info.append("O host não pertence à rede: Não")
        return info
    except Exception as e:
        return [f"Erro: {e}"]

    
def main(page: ft.Page):
    page.title =" Verificar Ip e Rede"
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

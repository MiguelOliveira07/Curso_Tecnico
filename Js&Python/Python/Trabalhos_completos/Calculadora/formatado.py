import flet as ft
import ipaddress as ip


def ip_host(meu_ip):
    endereco_host = ip.IPv4Address(meu_ip)
    return endereco_host


def ip_rede(meu_ip):
    endereco_rede = ip.IPv4Network(meu_ip, strict=False)
    info = [
        f"Endereço de rede: {endereco_rede}",
        f"Broadcast: {endereco_rede.broadcast_address}",
        f"IP da rede: {endereco_rede.network_address}",
        f"Máscara: {endereco_rede.with_netmask}",
    ]
    return endereco_rede.network_address, info


def verificar_host(host, rede):
    try:
        rede_address, info = ip_rede(rede)
        ip_host(host)
        if ip.IPv4Address(host) in ip.IPv4Network(rede, strict=False):
            info.append("O host pertence à rede: Sim ")
        else:
            info.append("O host não pertence à rede: Não ")
        return info
    except Exception as e:
        return [f"Erro: {e}"]


def main(page: ft.Page):
    page.title = "Verificador de IP e Rede"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    resultado_lista = ft.ListView(expand=True, spacing=5)

    def add_clicked(e):
        resultado_lista.controls.clear()
        meu_host = new_host.value.strip()
        meu_rede = new_rede.value.strip()

        # Validação básica
        if not meu_host or not meu_rede:
            page.snack_bar = ft.SnackBar(
                ft.Text("Informe o IP do host e da rede."),
                bgcolor=ft.Colors.RED_400,
            )
            page.snack_bar.open = True
        else:
            info = verificar_host(meu_host, meu_rede)
            if len(info) == 1 and info[0].startswith("Erro:"):
                page.snack_bar = ft.SnackBar(
                    ft.Text(info[0]),
                    bgcolor=ft.Colors.RED_400,
                )
                page.snack_bar.open = True
            else:
                for item in info:
                    resultado_lista.controls.append(ft.Text(item, size=15))

        new_host.value = ""
        new_rede.value = ""
        page.update()

    new_host = ft.TextField(
        hint_text="Entre com um IP de HOST válido:",
        width=350,
        border_color=ft.Colors.BLUE_400,
    )

    new_rede = ft.TextField(
        hint_text="Entre com um IP de REDE válido (ex: 192.168.0.0/24):",
        width=350,
        border_color=ft.Colors.BLUE_400,
    )

    add_button = ft.FloatingActionButton(
        icon=ft.Icons.SEARCH,
        bgcolor=ft.Colors.BLUE_400,
        on_click=add_clicked,
    )

    page.add(
        ft.Column(
            [
                ft.Text("Verificador de Host e Rede", size=22, weight=ft.FontWeight.BOLD),
                new_host,
                new_rede,
                add_button,
                ft.Divider(),
                ft.Text("Resultados:", size=16, weight=ft.FontWeight.BOLD),
                resultado_lista,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


ft.app(main)

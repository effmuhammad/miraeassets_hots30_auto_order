import flet as ft


def read_orderlist(link):
    pass


def main(page: ft.Page):

    link_field = ft.TextField(label="Insert your orderlist (GSheet link)",
                              icon=ft.icons.LINK)

    col = ft.Column(spacing=0, controls=[
        link_field
    ])

    show_orderlist = ft.ElevatedButton(
        "Show Orderlist",
        on_click=lambda: ft.Text("Start"),
        height=50,
    )

    start_button = ft.ElevatedButton(
        "Run Order",
        on_click=lambda: ft.Text("Start"),
        height=50,
    )

    botton_row = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=0,
        controls=[show_orderlist, ft.Container(width=30), start_button]
    )

    page.add(col)
    page.add(botton_row)


ft.app(target=main)

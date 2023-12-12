import flet as ft
import pandas as pd


def read_orderlist(link):
    pass


def get_gsheet_data(gsheetid: str, sheetname: str) -> pd.DataFrame:
    gsheetid = "1JXhc5Ag8VEtsCmScDdJqEXYmY6FP8HIMNnRVjpTxIVE"
    sheet_name = "Sheet1"
    gsheet_url = f"https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df = pd.read_csv(gsheet_url)
    return df


def get_localsheet_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def print_test(control):
    print("triggered")


def main(page: ft.Page):
    link_field = ft.TextField(
        label="Insert your orderlist (GSheet link)",
        icon=ft.icons.LINK,
        on_focus=print_test

    )

    input_selection = ft.Column(
        spacing=15,
        controls=[
            link_field,
            link_field
        ]
    )

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

    main_col = ft.Column(
        spacing=15,
        controls=[
            input_selection,
            botton_row
        ]
    )

    page.padding = 20
    page.window_width = 400
    page.window_height = 500
    page.window_min_width = 400
    page.window_min_height = 500
    page.add(main_col)
    page.add(
        ft.FloatingActionButton(
            icon=ft.icons.SETTINGS,
        )
    )


ft.app(target=main)

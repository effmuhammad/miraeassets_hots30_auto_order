import flet as ft
import pandas as pd


class HomeScreen(ft.UserControl):
    def __init__(self) -> None:
        super().__init__()

    def read_orderlist(self, link):
        pass

    def get_gsheet_data(self, gsheetid: str, sheetname: str) -> pd.DataFrame:
        gsheetid = "1JXhc5Ag8VEtsCmScDdJqEXYmY6FP8HIMNnRVjpTxIVE"
        sheet_name = "Sheet1"
        gsheet_url = f"https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        df = pd.read_csv(gsheet_url)
        return df

    def get_localsheet_data(self, path: str) -> pd.DataFrame:
        df = pd.read_csv(path)
        return df

    def print_test(self, control):
        print("triggered")

    def build(self):
        link_field = ft.TextField(
            label="Insert your orderlist (GSheet link)",
            icon=ft.icons.LINK,

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
        return main_col

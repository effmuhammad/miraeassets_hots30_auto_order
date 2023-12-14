import flet as ft
import pyautogui as pg


class SettingScreen(ft.UserControl):
    def __init__(self) -> None:
        super().__init__()

    def get_position(self, to_set: ft.Text):
        pos = pg.position()
        to_set.value = f"Position: {pos}"

    def set_button(self, to_set: ft.Text) -> ft.ElevatedButton:
        return ft.ElevatedButton(
            "Get Pos",
            on_click=self.get_position(to_set),
            height=50,
        )

    def build(self):
        pos_text = ft.Text("Position")

        main_col = ft.Column(
            spacing=15,
            controls=[
                ft.Text("Setting screen"),
                pos_text,
                self.set_button(pos_text),
            ]
        )
        return main_col

import flet as ft
import pyautogui as pg
import asyncio


class SettingScreen(ft.UserControl):
    def __init__(self) -> None:
        super().__init__()

    def set_button(self, to_set: ft.Text) -> ft.ElevatedButton:
        return ft.ElevatedButton(
            "Get Pos",
            height=50,
        )

    def build(self):
        pos_text = CursorPositionText()

        main_col = ft.Column(
            spacing=15,
            controls=[
                ft.Text("Setting screen"),
                pos_text,
                self.set_button(pos_text),
            ]
        )
        return main_col


class CursorPositionText(ft.UserControl):
    def __init__(self) -> None:
        super().__init__()
        self.value = "Position: "

    async def did_mount_async(self):
        print('did mount')
        self.running = True
        asyncio.create_task(self.update_cam())

    async def will_unmount_async(self):
        self.running = False

    async def update(self):
        while True:
            pos = pg.position()
            self.value = f"Position: {pos}"
            super().update()

    def build(self):
        return ft.Text(self.value)

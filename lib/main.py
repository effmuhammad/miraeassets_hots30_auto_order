import flet as ft
import pandas as pd
from src.screens.home_screen import *
from src.screens.setting_screen import *


async def clean_page(page: ft.Page):
    await page.clean_async()
    await page.update_async()


async def navigate(page: ft.Page, screen: ft.UserControl):
    await clean_page(page)
    await page.add_async(screen)
    await page.update_async()


async def main(page: ft.Page):
    page.padding = 20
    page.window_width = 400
    page.window_height = 500
    page.window_min_width = 400
    page.window_min_height = 500

    selected_file = ft.Text()

    async def pick_files_result(e: ft.FilePickerResultEvent):
        # selected_files.value = (
        #     ", ".join(map(lambda f: f.name, e.files)
        #               ) if e.files else "Cancelled!"
        # )
        selected_file.value = e.files[0].path
        await selected_file.update_async()

    async def browse_local_file(_):
        await pick_files_dialog.pick_files_async(allow_multiple=False)

    pick_files_dialog = ft.FilePicker(
        on_result=pick_files_result)

    page.overlay.append(pick_files_dialog)

    await navigate(page, HomeScreen(browse_local_file))

    await page.add_async(selected_file)

    # await page.add_async(ft.FloatingActionButton(
    #     icon=ft.icons.SETTINGS,
    #     on_click=navigate(page, SettingScreen()),
    # ))


ft.app(target=main)

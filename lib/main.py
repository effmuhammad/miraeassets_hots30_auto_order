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

    await navigate(page, HomeScreen())

    # await page.add_async(ft.FloatingActionButton(
    #     icon=ft.icons.SETTINGS,
    #     on_click=navigate(page, SettingScreen()),
    # ))


ft.app(target=main)

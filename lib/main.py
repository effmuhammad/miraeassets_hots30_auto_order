import flet as ft
import pandas as pd
from src.screens.home_screen import *
from src.screens.setting_screen import *


def clean_page(page: ft.Page):
    page.clean()
    page.update()


def navigate(page: ft.Page, screen: ft.UserControl):
    clean_page(page)
    page.add(screen)
    page.update()


def main(page: ft.Page):
    page.padding = 20
    page.window_width = 400
    page.window_height = 500
    page.window_min_width = 400
    page.window_min_height = 500

    navigate(page, HomeScreen())

    page.add(ft.FloatingActionButton(
        icon=ft.icons.SETTINGS,
        on_click=navigate(page, SettingScreen()),
    ))


ft.app(target=main)

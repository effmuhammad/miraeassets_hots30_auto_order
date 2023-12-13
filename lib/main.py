import flet as ft
import pandas as pd
from src.screens.home_screen import *


def main(page: ft.Page):
    page.padding = 20
    page.window_width = 400
    page.window_height = 500
    page.window_min_width = 400
    page.window_min_height = 500

    page.add(HomeScreen())


ft.app(target=main)

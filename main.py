import flet as ft
import webbrowser

def main(page: ft.Page):
    page.title = "تتبع الهاتف"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 30

    def open_android_tracker(e):
        webbrowser.open("https://www.google.com/android/find")

    def open_apple_tracker(e):
        webbrowser.open("https://www.icloud.com/find")

    title = ft.Text("اختر نوع جهازك لتتبع الهاتف", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
    android_button = ft.ElevatedButton("هاتف أندرويد", on_click=open_android_tracker, width=250, height=50, bgcolor=ft.colors.GREEN_600, color=ft.colors.WHITE)
    apple_button = ft.ElevatedButton("هاتف آيفون", on_click=open_apple_tracker, width=250, height=50, bgcolor=ft.colors.BLUE_600, color=ft.colors.WHITE)
    footer = ft.Text("هذه الخدمة تعتمد على مواقع Google و Apple الرسمية", size=12, color=ft.colors.GREY)

    page.add(
        title,
        ft.Column(
            [android_button, apple_button],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        footer
    )

ft.app(target=main)

print("hola mundo")

import reflex as rx

def index():
    return rx.vstack(
        rx.heading("Hola Mundo con Reflex", size="9"),
        rx.text("¡Bienvenido a mi primera aplicación web!"),
        rx.button("Haz clic aquí", on_click=lambda: print("Botón presionado"))
    )

app = rx.App()
app.add_page(index)


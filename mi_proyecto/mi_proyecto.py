"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx

class State(rx.State):
    clicked: bool = False

    def do_click(self):
        self.clicked = True

def index():
    return rx.vstack(
        rx.heading("Hola Mundo con Reflex", size="9"),
        rx.text("¡Bienvenido a mi primera aplicación web!"),
        rx.button("Haz clic aquí", on_click=State.do_click),
        rx.text(rx.cond(State.clicked, "¡Botón presionado!", ""))
    )

app = rx.App()
app.add_page(index)




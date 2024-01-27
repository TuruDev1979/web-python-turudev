import reflex as rx


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.hstack(
        rx.text(
            "TuruDev",
            height="40px"
        ),
        position="sticky",
        bg="blue",
        padding="16px",
        z_index="999"
    )


app = rx.App()
app.add_page(index)
app.compile()

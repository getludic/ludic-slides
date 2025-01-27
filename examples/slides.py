from ludic.catalog.headers import H1, H2
from ludic.catalog.lists import Item, List
from ludic.catalog.typography import Code, CodeBlock, Paragraph
from ludic_slides import Slide, SlideMain, Slides

slides = Slides(
    SlideMain(
        H1("The Ludic Framework"),
        Paragraph("Web Development in Pure Python with Type-Guided Components.")
    ),
    Slide(
        H2("Code Example"),
        CodeBlock(
            '''
            from ludic.catalog.layouts import Box
            from ludic.catalog.typography import Link
            from ludic.web import LudicApp

            app = LudicApp()

            @app.get("/")
            async def index() -> Box:
                """Homepage endpoint greeting visitors."""
                return Box(
                    f"Welcome to {Link("Ludic", to="/")}!",
                )
            ''',
            language="python"
        )
    ),
    Slide(
        H2("Quick Start"),
        Paragraph("Here are the commands you need to know:"),
        List(
            Item(Code("pip install ludic-slides")),
            Item(Code("ludic-slides slides.py")),
        )
    ),
)
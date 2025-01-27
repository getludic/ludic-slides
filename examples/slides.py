from ludic_slides import Slide, SlideMain, Slides
from ludic_slides.components import Code, CodeBlock, Header, Item, List, Paragraph

slides = Slides(
    SlideMain(
        Header("The Ludic Framework"),
        Paragraph("Web Development in Pure Python with Type-Guided Components."),
    ),
    Slide(
        Header("Code Example"),
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
            language="python",
        ),
    ),
    Slide(
        Header("Quick Start"),
        Paragraph("Here are the commands you need to know:"),
        List(
            Item(Code("pip install ludic-slides")),
            Item(Code("ludic-slides slides.py")),
        ),
    ),
)

from ludic.catalog.headers import H1, H2
from ludic.catalog.typography import CodeBlock, Paragraph
from ludic_slides import Slide, SlideMain, Slides


def test_generate_slides() -> None:
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
            H2("Test 3"),
        ),
    )
    with open("/Users/pavel.dedik/Downloads/slides.html", "w") as fd:
        fd.write(slides.to_html())


if __name__ == "__main__":
    test_generate_slides()
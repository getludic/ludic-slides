from ludic_slides import Slide, SlideMain, Slides
from ludic_slides.components import CodeBlock, Header, Paragraph


def test_generate_slides() -> None:
    slides = Slides(
        SlideMain(
            Header("The Ludic Framework"),
            Paragraph("Web Development in Pure Python with Type-Guided Components."),
        ),
        Slide(
            Header("Code Example"),
            CodeBlock("app = LudicApp()", language="python"),
        ),
        Slide(Header("Test 3")),
    )

    assert "The Ludic Framework" in slides.to_html()

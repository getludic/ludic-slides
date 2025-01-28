from ludic_slides import Slide, SlideMain, Slides
from ludic_slides.components import (
    Code,
    CodeBlock,
    Header,
    Item,
    Link,
    List,
    NumberedList,
    Paragraph,
)

slides = Slides(
    SlideMain(
        Header("Ludic Slides"),
        Paragraph(
            f"Building presentations with {Link('Ludic', to='https://getludic.dev')} "
            "in Python."
        ),
    ),
    Slide(
        Header("Getting Started"),
        NumberedList(
            Item(
                "Install Ludic Slides from PyPi",
                List(Item(Code("pip install ludic-slides"))),
            ),
            Item(
                f"Create a new file {Code('myslides.py')} with the following content:",
                List(
                    Item(
                        CodeBlock(
                            """
                            from ludic_slides import Slide, SlideMain, Slides

                            slides = Slides(
                                SlideMain(...),
                                Slide(...),
                                Slide(...)
                            )
                            """,
                            language="python",
                        )
                    )
                ),
            ),
            Item(
                "Compile the slides to HTML:",
                List(Item(Code("$ ludic-slides myslides.py"))),
            ),
            Item(
                "Open the slides in your browser:",
                List(Item(Code("$ open 'myslides.html'"))),
            ),
        ),
    ),
    Slide(
        Header("Slides"),
        List(
            Item(
                f"There are only two kinds of slides - {Code('SlideMain')} and "
                f"{Code('Slide')}",
            ),
            Item(
                f"The {Code('SlideMain')} is the opening slide (the first one in this "
                "presentation) and can only have one or two children - the "
                f"{Code('Header')} and optionally the {Code('Paragraph')} (subtitle)."
            ),
            Item(
                f"The {Code('Slide')} is the content slide (the rest of the slides "
                f"in this presentation) and must contain the {Code('Header')}) "
                "element, the rest can be any number of content elements."
            ),
        ),
        CodeBlock(
            """
            from ludic_slides import Slide, SlideMain, Slides
            from ludic_slides.components import Header, Paragraph, List, Item

            slides = Slides(
                SlideMain(Header("My Presentation")),
                Slide(
                    Header("Title"),
                    List(Item("First Point"), Item("Second Point")),
                ),
            )
            """,
            language="python",
        ),
    ),
    title="Ludic Slides Presentation",
)

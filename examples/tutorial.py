from ludic.html import b, i
from ludic_slides import Slide, SlideMain, Slides
from ludic_slides.components import (
    Code,
    CodeBlock,
    Header,
    Item,
    Link,
    List,
    Message,
    MessageSuccess,
    NumberedList,
    Paragraph,
    Table,
    TableHead,
    TableRow,
    Title,
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
                List(Code("pip install ludic-slides")),
            ),
            Item(
                f"Create a new file {Code('myslides.py')} with the following content:",
                List(
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
                ),
            ),
            Item(
                "Compile the slides to HTML:",
                List(Code("$ ludic-slides myslides.py")),
            ),
            Item(
                "Open the slides in your browser:",
                List(Code("$ open 'myslides.html'")),
            ),
        ),
    ),
    Slide(
        Header("Slides"),
        List(
            (
                f"There are only two kinds of slides - {Code('SlideMain')} and "
                f"{Code('Slide')}"
            ),
            (
                f"The {Code('SlideMain')} is the opening slide (the first one in this "
                "presentation) and can only have one or two children - the "
                f"{Code('Header')} and optionally the {Code('Paragraph')} (subtitle)."
            ),
            (
                f"The {Code('Slide')} is the content slide (the rest of the slides "
                f"in this presentation) and must contain the {Code('Header')}) "
                "element, the rest can be any number of content elements."
            ),
        ),
        CodeBlock(
            """
            from ludic_slides import Slide, SlideMain, Slides
            from ludic_slides.components import Header, Paragraph, List

            slides = Slides(
                SlideMain(Header("My Presentation")),
                Slide(
                    Header("Title"),
                    List("First Point", "Second Point"),
                ),
            )
            """,
            language="python",
        ),
    ),
    Slide(
        Header("Bulleted and Numbered Lists"),
        List(
            f"{Code('List')} creates a bulleted list",
            f"{Code('NumberedList')} creates a numbered list",
            f"Nested lists can be created with {Code('Item')}",
        ),
        CodeBlock(
            """
            from ludic_slides.components import Item, List, NumberedList

            List("First Item", "Second Item")
            NumberedList("First Item", "Second Item")

            List(
                Item(
                    "First Item",
                    List("First Subitem", "Second Subitem"),
                ),
                Item("Second Item"),
            )
            """,
            language="python",
        ),
    ),
    Slide(
        Header("Typography"),
        List(
            (
                f"{Code('b')} for {b('bold')}, {Code('i')} for {i('italic')}, "
                f"{Code('u')} for {i('underline')}"
            ),
            f"{Code('Link')} to create a hyperlink",
            f"{Code('Code')} and {Code('CodeBlock')} for code block",
        ),
        CodeBlock(
            """
            from ludic.html import i, b, u
            from ludic_slides.components import Paragraph, Code, CodeBlock, Link

            Paragraph(i("italic"), b("bold"), u("underline"))
            Link("Example Link", to="https://example.com")
            Code("pip install ludic-slides")
            CodeBlock(
                \"\"\"
                def inc(n: int) -> int:
                    return n + 1
                \"\"\",
                language="python"
            )
            """,
            language="python",
        ),
    ),
    Slide(
        Header("Tables"),
        Paragraph(
            f"Here is a simple table created with the {Code('Table')} component:"
        ),
        Table(
            TableHead("ID", "Name", "ELO rating"),
            TableRow("1", "DeepSeek-R1", "1361"),
            TableRow("2", "Gemini-2.0-Flash", "1355"),
            TableRow("3", "o3-mini", "1307"),
        ),
        CodeBlock(
            """
            from ludic_slides.components import Table, TableHead, TableRow

            Table(
                TableHead("ID", "Name", "ELO rating"),
                TableRow("1", "o1", "1363"),
                TableRow("2", "deepseek-r1", "1368"),
            )
            """,
            language="python",
        ),
    ),
    Slide(
        Header("Messages"),
        Message("Simple message."),
        MessageSuccess(Title("A title"), "A message with a title."),
        CodeBlock(
            """
            from ludic_slides.components import (
                Message, MessageInfo, MessageDanger, MessageSuccess, MessageWarning,
                Title
            )

            Message("Simple message.")
            MessageInfo(Title("Info"), "Danger message with a title.")
            MessageSuccess(Title("Success"), "Danger message with a title.")
            MessageWarning(Title("Warning"), "Danger message with a title.")
            MessageDanger(Title("Danger"), "Danger message with a title.")
            """,
            language="python",
        ),
    ),
    title="Ludic Slides Presentation",
)

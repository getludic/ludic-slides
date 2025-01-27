# Ludic Slides

Create fast presentations with [Ludic](https://getludic.dev).

## Installation

```
pip install ludic-slides
```

## Quick Start

Create a new file `slides.py` with the following content:

```python
from ludic.catalog.headers import H1, H2
from ludic.catalog.typography import Paragraph, Code
from ludic.catalog.items import List, Item
from ludic_slides import Slide, SlideMain, Slides

slides = Slides(
    SlideMain(
        H1("My Slides"),
        Paragraph("Quickstart for Ludic Slides"),
    ),
    Slide(
        H2("Installation"),
        List(
            Item(Code("pip install ludic-slides")),
            Item(Code("ludic-slides slides.py")),
        )
    ),
)
```

## Generate HTML slides

```
ludic-slides slides.py
```

You can also specify the output path:

```
ludic-slides slides.py -o ~/Documents/my-slides.py
```

If the variable's name in the `slides.py` file does not equal `slides`, you can also specify a different name:

```
ludic-slides file-name.py:my_variable
```

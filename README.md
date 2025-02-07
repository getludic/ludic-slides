# Ludic Slides

Building presentations with [Ludic](https://getludic.dev) in Python.

![](./assets/example.png)

## Installation

```
pip install ludic-slides
```

## Quick Start

Create a new file `slides.py` with the following content:

```python
from ludic_slides import Slide, SlideMain, Slides
from ludic_slides.components import Code, Header, Item, List, Paragraph

slides = Slides(
    SlideMain(
        Header("My Slides"),
        Paragraph("A Quick Start for Ludic Slides"),
    ),
    Slide(
        Header("Installation"),
        List(
            Item(Code("$ pip install ludic-slides")),
            Item(Code("$ ludic-slides slides.py")),
        )
    ),
)
```

## Generate HTML Slides

The following command generates `slides.html` file:

```
ludic-slides slides.py
```

If the variable's name in the `slides.py` file does not equal `slides`, you can also specify a different name:

```
ludic-slides file-name.py:my_variable
```

You can also specify the output path:

```
ludic-slides slides.py -o ~/Documents/my-slides.html
```

> [!NOTE]
> Note that outputting to a different location means you will need to copy static files like images used in your presentation to the correct location manually.

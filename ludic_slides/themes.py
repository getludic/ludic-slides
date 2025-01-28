from dataclasses import dataclass, field

from ludic.styles.themes import Borders, Fonts, Header, Headers, Sizes, Theme
from ludic.styles.types import Size


@dataclass
class SlidesTheme(Theme):
    """Slide configuration."""

    name: str = "slide"

    measure: Size = Size(100, "%")
    aspect_ratio: tuple[int, int] = (4, 3)
    fonts: Fonts = field(default_factory=lambda: Fonts(size=Size(3, "vmin")))
    headers: Headers = field(
        default_factory=lambda: Headers(
            h1=Header(size=Size(6, "vmin"), anchor=False),
            h2=Header(size=Size(5, "vmin"), anchor=False),
            h3=Header(size=Size(4, "vmin"), anchor=False),
        )
    )
    borders: Borders = field(
        default_factory=lambda: Borders(
            thin=Size(0.05, "rem"),
            normal=Size(0.1, "rem"),
            thick=Size(0.2, "rem"),
        )
    )
    sizes: Sizes = field(
        default_factory=lambda: Sizes(
            xxxxs=Size(0.2, "vmin"),
            xxxs=Size(0.3, "vmin"),
            xxs=Size(0.5, "vmin"),
            xs=Size(0.9, "vmin"),
            s=Size(1.2, "vmin"),
            m=Size(1.6, "vmin"),
            l=Size(2, "vmin"),
            xl=Size(2.3, "vmin"),
            xxl=Size(3, "vmin"),
            xxxl=Size(4, "vmin"),
            xxxxl=Size(6, "vmin"),
        )
    )

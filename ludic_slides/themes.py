from dataclasses import dataclass, field

from ludic.styles.themes import Borders, Fonts, Header, Headers, Sizes, Theme
from ludic.styles.types import Size


@dataclass
class SlidesTheme(Theme):
    """Theme configuration for slide presentations.

    Defines the visual styling and layout parameters for slides including
    dimensions, fonts, headers, borders, and various size presets.

    Attributes:
        name: Theme identifier name
        measure: Size specification for the slide width
        aspect_ratio: Tuple defining slide dimensions (width, height)
        fonts: Font configuration including base size
        headers: Configuration for h1-h3 headers including size and anchor settings
        borders: Border width definitions for thin, normal, and thick borders
        sizes: Collection of predefined size values from xxxxs to xxxxl
    """

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

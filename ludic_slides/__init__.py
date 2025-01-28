from ludic.styles.themes import set_default_theme

from .components import Slide, SlideMain, Slides
from .themes import SlidesTheme

set_default_theme(SlidesTheme())

__all__ = (
    "Slide",
    "SlideMain",
    "Slides",
)

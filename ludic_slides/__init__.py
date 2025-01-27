from ludic.styles import themes

from .components import Slide, SlideMain, Slides
from .theme import SlidesTheme

themes.set_default_theme(SlidesTheme())

__all__ = (
    "Slide",
    "SlideMain",
    "Slides",
)

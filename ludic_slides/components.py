from typing import override

from ludic.attrs import Attrs, NoAttrs
from ludic.catalog.headers import H1, H2
from ludic.catalog.layouts import Stack
from ludic.catalog.pages import Body, Head, HtmlPage
from ludic.catalog.typography import Paragraph
from ludic.components import Component, ComponentStrict
from ludic.html import div, meta, script, style
from ludic.styles import types
from ludic.types import AnyChildren, JavaScript

from .theme import SlidesTheme


class Slide(ComponentStrict[H2, *tuple[AnyChildren, ...], NoAttrs]):
    """A component used to create a slide in a presentation."""

    classes = ["slide"]
    styles = style[SlidesTheme].use(
        lambda theme: {
            ".slide": {
                "position": "absolute",
                "inset": "0",
                "margin": "auto",
                "max-width": "100%",
                "max-height": "100%",
                "aspect-ratio": "/".join(map(str, theme.aspect_ratio)),
            },
            ".slide-content": {
                "height": f"calc(100% - {theme.sizes.xxxl})",
                "border-radius": theme.sizes.xs,
                "background-color": theme.colors.white,
                "box-shadow": (
                    f"0 {theme.sizes.xs} {theme.sizes.s} {theme.colors.light.darken(3)}"
                ),
                "font-size": theme.sizes.xxl,
                "padding-inline": theme.sizes.xxxl,
                "padding-block": theme.sizes.xxl,
                "margin": theme.sizes.xl,
                "overflow": "hidden",
            },
            ".slide-content h1": {
                "text-align": "center",
            },
        }
    )

    @override
    def render(self) -> div:
        return div(
            div(
                div(Stack(*self.children), classes=["slide-regular"]),
                classes=["slide-content"],
            )
        )


class SlideMain(ComponentStrict[H1, *tuple[Paragraph, ...], NoAttrs]):
    """A component used to create a main slide in a presentation."""

    classes = ["slide"]
    styles = {
        ".slide-main": {
            "display": "flex",
            "align-items": "center",
            "justify-content": "center",
            "height": "100%",
        },
    }

    @override
    def render(self) -> div:
        return div(
            div(
                div(Stack(*self.children), classes=["slide-main"]),
                classes=["slide-content"],
            )
        )


class SlidesAttrs(Attrs, total=False):
    title: str


class Slides(Component[Slide | SlideMain, SlidesAttrs]):
    """A component rendering as a slideshow.

    Example usage:

        Slides(
            Slide(...),
            Slide(...),
            Slide(...),
        )
    """

    classes = ["slides"]
    styles = style[SlidesTheme].use(
        lambda theme: {
            ".slides": {
                "background-color": theme.colors.light,
                "min-height": types.Size(100, "vh"),
                "position": "relative",
            }
        }
    )
    javascript = JavaScript(
        """
        document.addEventListener('DOMContentLoaded', () => {
            const slides = document.querySelectorAll('.slide');

            if (!slides.length) return;

            const getSlideNumberFromHash = () => {
                const hash = window.location.hash.slice(1);
                const n = parseInt(hash, 10);
                return !isNaN(n) && n > 0 && n <= slides.length ? n : 1;
            };

            const showSlide = (n) => {
                slides.forEach((slide, index) => {
                    slide.style.display = index + 1 === n ? 'block' : 'none';
                });
            };

            const navigateSlides = (direction) => {
                const currentSlide = getSlideNumberFromHash();
                const newSlide = currentSlide + direction;

                if (newSlide >= 1 && newSlide <= slides.length) {
                    window.location.hash = `#${newSlide}`;
                    showSlide(newSlide);
                }
            };

            // Initialize the slides
            showSlide(getSlideNumberFromHash());

            // Listen for hash changes (e.g., user navigates directly to a slide)
            window.addEventListener('hashchange', () => {
                showSlide(getSlideNumberFromHash());
            });

            // Keyboard navigation
            document.addEventListener('keydown', (event) => {
                if (event.key === 'ArrowRight') {
                    navigateSlides(1);
                } else if (event.key === 'ArrowLeft') {
                    navigateSlides(-1);
                }
            });

            document.addEventListener('click', (event) => {
                const viewportWidth = window.innerWidth;
                const clickedElement = event.target;

                // Check if click is outside any .slide element
                const isOutsideSlide = ![...slides].some(
                    slide => slide.contains(clickedElement));

                if (isOutsideSlide) {
                    if (event.clientX > viewportWidth / 2) {
                        navigateSlides(1);
                    } else {
                        navigateSlides(-1);
                    }
                }
            });
        });
        """
    )

    @override
    def render(self) -> HtmlPage:
        return HtmlPage(
            Head(
                meta(charset="utf-8"),
                meta(name="viewport", content="width=device-width, initial-scale=1.0"),
                title=self.attrs.get("title", "My Slides"),
            ),
            Body(
                div(*self.children, classes=self.classes),
                script(self.javascript, type="text/javascript"),
            ),
        )

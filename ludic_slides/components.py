from typing import override

from ludic import html
from ludic.attrs import Attrs, GlobalAttrs, NoAttrs
from ludic.catalog.headers import H1 as Header
from ludic.catalog.items import Key, Pairs, Value
from ludic.catalog.layouts import Stack
from ludic.catalog.lists import Item, List, NumberedList
from ludic.catalog.messages import (
    Message,
    MessageDanger,
    MessageInfo,
    MessageSuccess,
    MessageWarning,
    Title,
)
from ludic.catalog.pages import Body, Head, HtmlPage
from ludic.catalog.quotes import Quote
from ludic.catalog.tables import Table, TableHead, TableRow
from ludic.catalog.typography import Code, CodeBlock, Link, Paragraph
from ludic.components import Component, ComponentStrict
from ludic.html import div, meta, script, style
from ludic.styles import types
from ludic.types import ComplexChildren, JavaScript

from .themes import SlidesTheme

__all__ = (
    "Header",
    "Content",
    "Link",
    "List",
    "NumberedList",
    "Item",
    "Code",
    "CodeBlock",
    "Paragraph",
    "Slide",
    "SlideMain",
    "Slides",
    "Key",
    "Value",
    "Pairs",
    "Table",
    "TableHead",
    "TableRow",
    "Title",
    "Message",
    "MessageDanger",
    "MessageInfo",
    "MessageSuccess",
    "MessageWarning",
    "Quote",
)

type Content = (
    Code
    | CodeBlock
    | Link
    | List
    | NumberedList
    | Paragraph
    | Pairs
    | Table
    | Message
    | MessageDanger
    | MessageInfo
    | MessageSuccess
    | MessageWarning
    | Quote
    | html.a
    | html.b
    | html.s
    | html.i
    | html.strong
    | html.table
    | html.blockquote
    | html.ul
    | html.ol
    | html.dl
    | html.br
    | html.code
    | html.pre
    | html.em
)


class BaseSlide(Component[ComplexChildren, GlobalAttrs]):
    """An abstract component used as a base class for slide components."""

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
                "font-size": theme.fonts.size,
                "padding-inline": theme.sizes.xxxl,
                "padding-block": theme.sizes.xxl,
                "margin": theme.sizes.xl,
                "overflow": "hidden",
            },
            ".slide .stack > * + *": {
                "inline-size": "auto",
            },
            ".slide h1": {
                "text-align": "center",
            },
            (".slide .code-block", ".slide .code-block *", ".slide .code"): {
                "font-size": theme.fonts.size * 0.85,
            },
            (".slide .code-block", ".slide .code"): {
                "border": f"{theme.borders.thin} solid {theme.colors.light.darken(1)}",
                "border-radius": theme.sizes.xxs,
            },
            ".slide ul > li::marker": {
                "font-size": theme.fonts.size,
            },
            ".slide li": {
                "padding-inline-start": theme.sizes.xs,
            },
            (".slide ol", ".slide ul"): {
                "margin-inline-start": theme.sizes.s,
            },
            (".slide ol > li + li", ".slide ul > li + li"): {
                "margin-block-start": theme.sizes.m,
            },
        }
    )

    @override
    def render(self) -> div:
        return div(div(div(*self.children, **self.attrs), classes=["slide-content"]))


class Slide(ComponentStrict[Header, *tuple[Content, ...], NoAttrs]):
    """A component used to create a slide in a presentation."""

    @override
    def render(self) -> BaseSlide:
        return BaseSlide(Stack(*self.children), classes=["slide-regular"])


class SlideMain(ComponentStrict[Header, *tuple[Paragraph, ...], NoAttrs]):
    """A component used to create a main slide in a presentation."""

    styles = {
        ".slide-main": {
            "display": "flex",
            "align-items": "center",
            "justify-content": "center",
            "height": "100%",
        },
    }

    @override
    def render(self) -> BaseSlide:
        return BaseSlide(Stack(*self.children), classes=["slide-main"])


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

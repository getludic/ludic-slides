import argparse
import os
import sys
from typing import Any


def locate_and_render_slides(
    python_file_path: str,
    slides_variable: str = "slides",
    output_file: str = "slides.html",
) -> None:
    """Locates a 'slides' variable within a Python file and renders it to HTML.

    Args:
        python_file_path: The path to the Python file.
        slides_variable: The name of the variable containing the slides object.
        output_file: The path to the output HTML file.
    """
    if not os.path.isfile(python_file_path):
        print(f"Error: File '{python_file_path}' not found.")
        sys.exit(1)

    try:
        # Create a dictionary to hold locals, it will allow us to access variables in
        # the loaded module
        module_namespace: dict[str, Any] = {}
        # Execute file in a namespace
        with open(python_file_path, encoding="utf-8") as f:
            exec(f.read(), {}, module_namespace)  # noqa

    except Exception as e:
        print(f"Error loading file '{python_file_path}': {e}")
        sys.exit(1)

    if slides_variable not in module_namespace:
        print(
            f"Error: File '{python_file_path}' does not contain a variable "
            f"named '{slides_variable}'."
        )
        sys.exit(1)

    slides_obj = module_namespace[slides_variable]

    if not callable(getattr(slides_obj, "to_html", None)):
        print(
            f"Error: Variable '{slides_variable}' within file '{python_file_path}' "
            f"does not have a 'to_html' method"
        )
        sys.exit(1)
    try:
        html_content = slides_obj.to_html()
    except Exception as e:
        print(
            f"Error calling 'to_html' on variable '{slides_variable}' within "
            f"file '{python_file_path}': {e}"
        )
        sys.exit(1)
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Slides rendered to: {output_file}")
    except Exception as e:
        print(f"Error writing to file '{output_file}': {e}")
        sys.exit(1)


def create_parser() -> argparse.ArgumentParser:
    """Creates an argument parser for the CLI.

    Returns:
        An argparse.ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(description="Render slides from a Python file.")
    parser.add_argument(
        "file_path",
        help=(
            "Python file path and optionally variable name separated by a colon "
            "(e.g., my_slides.py:slides)"
        ),
    )
    parser.add_argument(
        "-o",
        "--output",
        required=False,
        help="Path to the output HTML file.",
        default="slides.html",
    )
    return parser


def main(args: list[str] | None = None) -> None:
    """Main function for the CLI.

    Args:
        args: A list of command line arguments (optional, will default to sys.argv).
    """
    if args is None:
        args = sys.argv[1:]

    parser = create_parser()
    args_parsed = parser.parse_args(args)

    try:
        if ":" not in args_parsed.file_path:
            python_file_path, slides_variable = args_parsed.file_path, "slides"
        else:
            python_file_path, slides_variable = args_parsed.file_path.split(":", 1)
    except ValueError:
        print(
            "Error: Invalid format for file_path. Use 'path/to/file.py' or "
            "path/to/file.py:slides_var'."
        )
        sys.exit(1)

    locate_and_render_slides(python_file_path, slides_variable, args_parsed.output)


if __name__ == "__main__":
    main()

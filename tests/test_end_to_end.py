"""End-to-end tests for every combination of options."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

import bs4
import pytest
from griffe.tests import temporary_pypackage
from inline_snapshot import external, outsource, snapshot

if TYPE_CHECKING:
    from mkdocstrings.handlers.python import PythonHandler

options = {
    # General options.
    "find_stubs_package": (True, False),
    "allow_inspection": (True, False),
    "show_bases": (True, False),
    "show_source": (True, False),
    "preload_modules": ([], ["mod1"], None),
    # Heading options.
    "heading_level": (1, 2, 3, 4, 5, 6),
    "show_root_heading": (True, False),
    "show_root_toc_entry": (True, False),
    "show_root_full_path": (True, False),
    "show_root_members_full_path": (True, False),
    "show_object_full_path": (True, False),
    "show_category_heading": (True, False),
    "show_symbol_type_heading": (True, False),
    "show_symbol_type_toc": (True, False),
    # Members options.
    "inherited_members": ([], ["a", "b"], True, False, None),
    "members": ([], ["a", "b"], True, False, None),
    "members_order": ("source", "alphabetical"),
    "filters": ([], ["!a"], ["a"], None),
    "group_by_category": (True, False),
    "show_submodules": (True, False),
    "summary": (True, False),  # TODO: Test dict.
    "show_labels": (True, False),
    # Docstrings options.
    "docstring_style": ("numpy", "google", "sphinx", None),
    "docstring_options": ({},),  # TODO: Add more examples.
    "docstring_section_style": ("table", "list", "spacy"),
    "merge_init_into_class": (True, False),
    "show_if_no_docstring": (True, False),
    "show_docstring_attributes": (True, False),
    "show_docstring_functions": (True, False),
    "show_docstring_classes": (True, False),
    "show_docstring_modules": (True, False),
    "show_docstring_description": (True, False),
    "show_docstring_examples": (True, False),
    "show_docstring_other_parameters": (True, False),
    "show_docstring_parameters": (True, False),
    "show_docstring_raises": (True, False),
    "show_docstring_receives": (True, False),
    "show_docstring_returns": (True, False),
    "show_docstring_warns": (True, False),
    "show_docstring_yields": (True, False),
    # Signature options.
    "annotations_path": ("brief", "source"),
    "line_length": (1, 10, 60, 120, 1000),
    "show_signature": (True, False),
    "show_signature_annotations": (True, False),
    "signature_crossrefs": (True, False),
    "separate_signature": (True, False),
    "unwrap_annotated": (True, False),
}


def _normalize_html(html: str) -> str:
    soup = bs4.BeautifulSoup(html, features="html.parser")
    html = soup.prettify()
    html = re.sub(r"\b(0x)[a-f0-9]+\b", r"\1...", html)
    html = re.sub(r"^(Build Date UTC ?:).+", r"\1...", html, flags=re.MULTILINE)
    html = re.sub(r"\b[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\b", r"...", html)
    html = re.sub(r'(?<=id="cell-id=)\w+(?=")', r"...", html)
    return html


snapshots = snapshot(
    {
        (
            ("annotations_path", "brief"),
            ("separate_signature", True),
            ("show_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
            ("unwrap_annotated", True),
        ): external("3603a08e7614*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", False),
            ("show_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
            ("unwrap_annotated", False),
        ): external("36a1a03a6364*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", False),
            ("show_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
            ("unwrap_annotated", False),
        ): external("011c334b854b*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", True),
            ("show_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
            ("unwrap_annotated", False),
        ): external("89c8c205249f*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", True),
            ("show_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
            ("unwrap_annotated", True),
        ): external("d552c9951139*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", True),
            ("show_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
            ("unwrap_annotated", False),
        ): external("da69cf4e2834*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", False),
            ("show_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
            ("unwrap_annotated", False),
        ): external("bd14e6a60af2*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", True),
            ("show_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
            ("unwrap_annotated", False),
        ): external("d944bd9f3d8c*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", True),
            ("show_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
            ("unwrap_annotated", True),
        ): external("c7fb0a797254*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", True),
            ("show_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
            ("unwrap_annotated", False),
        ): external("1531e41e8dbe*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", True),
            ("show_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
            ("unwrap_annotated", True),
        ): external("c7fb0a797254*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", False),
            ("show_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
            ("unwrap_annotated", True),
        ): external("36a1a03a6364*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", False),
            ("show_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
            ("unwrap_annotated", False),
        ): external("36a1a03a6364*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", True),
            ("show_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
            ("unwrap_annotated", False),
        ): external("d552c9951139*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", False),
            ("show_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
            ("unwrap_annotated", False),
        ): external("36a1a03a6364*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", True),
            ("show_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
            ("unwrap_annotated", True),
        ): external("d552c9951139*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", False),
            ("show_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
            ("unwrap_annotated", True),
        ): external("011c334b854b*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", False),
            ("show_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
            ("unwrap_annotated", False),
        ): external("36a1a03a6364*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", False),
            ("show_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
            ("unwrap_annotated", True),
        ): external("36a1a03a6364*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", False),
            ("show_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
            ("unwrap_annotated", True),
        ): external("36a1a03a6364*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", True),
            ("show_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
            ("unwrap_annotated", False),
        ): external("3603a08e7614*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", True),
            ("show_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
            ("unwrap_annotated", True),
        ): external("89c8c205249f*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", False),
            ("show_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
            ("unwrap_annotated", True),
        ): external("36a1a03a6364*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", False),
            ("show_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
            ("unwrap_annotated", False),
        ): external("bd14e6a60af2*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", True),
            ("show_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
            ("unwrap_annotated", True),
        ): external("da69cf4e2834*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", False),
            ("show_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
            ("unwrap_annotated", True),
        ): external("bd14e6a60af2*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", False),
            ("show_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
            ("unwrap_annotated", True),
        ): external("011c334b854b*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", False),
            ("show_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
            ("unwrap_annotated", False),
        ): external("36a1a03a6364*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", True),
            ("show_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
            ("unwrap_annotated", False),
        ): external("da69cf4e2834*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", False),
            ("show_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
            ("unwrap_annotated", True),
        ): external("36a1a03a6364*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", True),
            ("show_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
            ("unwrap_annotated", True),
        ): external("1531e41e8dbe*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", False),
            ("show_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
            ("unwrap_annotated", True),
        ): external("bd14e6a60af2*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", True),
            ("show_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
            ("unwrap_annotated", True),
        ): external("89c8c205249f*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", False),
            ("show_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
            ("unwrap_annotated", True),
        ): external("36a1a03a6364*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", True),
            ("show_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
            ("unwrap_annotated", True),
        ): external("d944bd9f3d8c*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", True),
            ("show_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
            ("unwrap_annotated", True),
        ): external("1531e41e8dbe*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", True),
            ("show_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
            ("unwrap_annotated", True),
        ): external("a1b8ff405bf2*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", False),
            ("show_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
            ("unwrap_annotated", True),
        ): external("bd14e6a60af2*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", False),
            ("show_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
            ("unwrap_annotated", False),
        ): external("36a1a03a6364*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", True),
            ("show_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
            ("unwrap_annotated", False),
        ): external("1531e41e8dbe*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", True),
            ("show_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
            ("unwrap_annotated", False),
        ): external("d944bd9f3d8c*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", True),
            ("show_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
            ("unwrap_annotated", False),
        ): external("d552c9951139*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", False),
            ("show_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
            ("unwrap_annotated", True),
        ): external("36a1a03a6364*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", True),
            ("show_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
            ("unwrap_annotated", True),
        ): external("3603a08e7614*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", True),
            ("show_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
            ("unwrap_annotated", False),
        ): external("a1b8ff405bf2*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", False),
            ("show_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
            ("unwrap_annotated", False),
        ): external("36a1a03a6364*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", False),
            ("show_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
            ("unwrap_annotated", False),
        ): external("bd14e6a60af2*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", True),
            ("show_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
            ("unwrap_annotated", False),
        ): external("3603a08e7614*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", True),
            ("show_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
            ("unwrap_annotated", False),
        ): external("a1b8ff405bf2*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", False),
            ("show_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
            ("unwrap_annotated", True),
        ): external("36a1a03a6364*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", False),
            ("show_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
            ("unwrap_annotated", True),
        ): external("011c334b854b*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", True),
            ("show_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
            ("unwrap_annotated", True),
        ): external("a1b8ff405bf2*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", False),
            ("show_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
            ("unwrap_annotated", False),
        ): external("36a1a03a6364*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", False),
            ("show_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
            ("unwrap_annotated", False),
        ): external("bd14e6a60af2*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", False),
            ("show_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
            ("unwrap_annotated", True),
        ): external("bd14e6a60af2*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", True),
            ("show_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
            ("unwrap_annotated", False),
        ): external("c7fb0a797254*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", True),
            ("show_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
            ("unwrap_annotated", False),
        ): external("89c8c205249f*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", True),
            ("show_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
            ("unwrap_annotated", False),
        ): external("c7fb0a797254*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", False),
            ("show_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
            ("unwrap_annotated", False),
        ): external("011c334b854b*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", False),
            ("show_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
            ("unwrap_annotated", False),
        ): external("011c334b854b*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", True),
            ("show_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
            ("unwrap_annotated", True),
        ): external("d944bd9f3d8c*.html"),
        (
            ("annotations_path", "source"),
            ("separate_signature", True),
            ("show_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
            ("unwrap_annotated", True),
        ): external("da69cf4e2834*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", False),
            ("show_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
            ("unwrap_annotated", False),
        ): external("011c334b854b*.html"),
        (
            ("annotations_path", "brief"),
            ("separate_signature", False),
            ("show_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
            ("unwrap_annotated", True),
        ): external("011c334b854b*.html"),
    },
)


# General options.
# @pytest.mark.parametrize("find_stubs_package", options["find_stubs_package"])
# @pytest.mark.parametrize("allow_inspection", options["allow_inspection"])
# @pytest.mark.parametrize("show_bases", options["show_bases"])
# @pytest.mark.parametrize("show_source", options["show_source"])
# @pytest.mark.parametrize("preload_modules", options["preload_modules"])
# Heading options.
# @pytest.mark.parametrize("heading_level", options["heading_level"])
# @pytest.mark.parametrize("show_root_heading", options["show_root_heading"])
# @pytest.mark.parametrize("show_root_toc_entry", options["show_root_toc_entry"])
# @pytest.mark.parametrize("show_root_full_path", options["show_root_full_path"])
# @pytest.mark.parametrize("show_root_members_full_path", options["show_root_members_full_path"])
# @pytest.mark.parametrize("show_object_full_path", options["show_object_full_path"])
# @pytest.mark.parametrize("show_category_heading", options["show_category_heading"])
# @pytest.mark.parametrize("show_symbol_type_heading", options["show_symbol_type_heading"])
# @pytest.mark.parametrize("show_symbol_type_toc", options["show_symbol_type_toc"])
# Members options.
# @pytest.mark.parametrize("inherited_members", options["inherited_members"])
# @pytest.mark.parametrize("members", options["members"])
# @pytest.mark.parametrize("members_order", options["members_order"])
# @pytest.mark.parametrize("filters", options["filters"])
# @pytest.mark.parametrize("group_by_category", options["group_by_category"])
# @pytest.mark.parametrize("show_submodules", options["show_submodules"])
# @pytest.mark.parametrize("summary", options["summary"])
# @pytest.mark.parametrize("show_labels", options["show_labels"])
# Docstrings options.
# @pytest.mark.parametrize("docstring_style", options["docstring_style"])
# @pytest.mark.parametrize("docstring_options", options["docstring_options"])
# @pytest.mark.parametrize("docstring_section_style", options["docstring_section_style"])
# @pytest.mark.parametrize("merge_init_into_class", options["merge_init_into_class"])
# @pytest.mark.parametrize("show_if_no_docstring", options["show_if_no_docstring"])
# @pytest.mark.parametrize("show_docstring_attributes", options["show_docstring_attributes"])
# @pytest.mark.parametrize("show_docstring_functions", options["show_docstring_functions"])
# @pytest.mark.parametrize("show_docstring_classes", options["show_docstring_classes"])
# @pytest.mark.parametrize("show_docstring_modules", options["show_docstring_modules"])
# @pytest.mark.parametrize("show_docstring_description", options["show_docstring_description"])
# @pytest.mark.parametrize("show_docstring_examples", options["show_docstring_examples"])
# @pytest.mark.parametrize("show_docstring_other_parameters", options["show_docstring_other_parameters"])
# @pytest.mark.parametrize("show_docstring_parameters", options["show_docstring_parameters"])
# @pytest.mark.parametrize("show_docstring_raises", options["show_docstring_raises"])
# @pytest.mark.parametrize("show_docstring_receives", options["show_docstring_receives"])
# @pytest.mark.parametrize("show_docstring_returns", options["show_docstring_returns"])
# @pytest.mark.parametrize("show_docstring_warns", options["show_docstring_warns"])
# @pytest.mark.parametrize("show_docstring_yields", options["show_docstring_yields"])
# Signature options
@pytest.mark.parametrize("annotations_path", options["annotations_path"])
# @pytest.mark.parametrize("line_length", options["line_length"])
@pytest.mark.parametrize("show_signature", options["show_signature"])
@pytest.mark.parametrize("show_signature_annotations", options["show_signature_annotations"])
@pytest.mark.parametrize("signature_crossrefs", options["signature_crossrefs"])
@pytest.mark.parametrize("separate_signature", options["separate_signature"])
@pytest.mark.parametrize("unwrap_annotated", options["unwrap_annotated"])
def test_end_to_end(
    handler: PythonHandler,
    # find_stubs_package: bool,
    # allow_inspection: bool,
    # show_bases: bool,
    # show_source: bool,
    # preload_modules: list[str] | None,
    # heading_level: int,
    # show_root_heading: bool,
    # show_root_toc_entry: bool,
    # show_root_full_path: bool,
    # show_root_members_full_path: bool,
    # show_object_full_path: bool,
    # show_category_heading: bool,
    # show_symbol_type_heading: bool,
    # show_symbol_type_toc: bool,
    # inherited_members: list[str] | bool | None,
    # members: list[str] | bool | None,
    # members_order: str,
    # filters: list[str] | None,
    # group_by_category: bool,
    # show_submodules: bool,
    # summary: bool | dict[str, bool] | None,
    # show_labels: bool,
    # docstring_style: str,
    # docstring_options: dict[str, str] | None,
    # docstring_section_style: str,
    # merge_init_into_class: bool,
    # show_if_no_docstring: bool,
    # show_docstring_attributes: bool,
    # show_docstring_functions: bool,
    # show_docstring_classes: bool,
    # show_docstring_modules: bool,
    # show_docstring_description: bool,
    # show_docstring_examples: bool,
    # show_docstring_other_parameters: bool,
    # show_docstring_parameters: bool,
    # show_docstring_raises: bool,
    # show_docstring_receives: bool,
    # show_docstring_returns: bool,
    # show_docstring_warns: bool,
    # show_docstring_yields: bool,
    annotations_path: str,
    # line_length: int,
    show_signature: bool,
    show_signature_annotations: bool,
    signature_crossrefs: bool,
    separate_signature: bool,
    unwrap_annotated: bool,
) -> None:
    """Test rendering of a given theme's templates.

    Parameters:
        identifier: Parametrized identifier.
        handler: Python handler (fixture).
    """
    final_options = {**locals()}
    final_options.pop("handler")
    handler_options = final_options.copy()
    code = """
        def foo(a: int, b: str) -> None:
            '''Docstring for `foo`.'''

        class Bar:
            '''Docstring for `Bar`.'''

            def __init__(self, a: int, b: str) -> None:
                '''Docstring for `Bar.__init__`.'''
                self.c = a + b
                '''Docstring for `Bar.c`.'''

            def foo(self, a: int, b: str) -> None:
                '''Docstring.'''

        baz: int = 42
        '''Docstring for `baz`.'''

        class Qux(Bar):
            '''Docstring for `Qux`.'''
    """
    with temporary_pypackage("pkg", {"__init__.py": code}) as tmppkg:
        handler._paths.insert(0, tmppkg.tmpdir)
        data = handler.collect("pkg", handler_options)
        html = handler.render(data, handler_options)
        html = _normalize_html(html)
        snapshot_key = tuple(sorted(final_options.items()))
        assert outsource(html, suffix=".html") == snapshots[snapshot_key]

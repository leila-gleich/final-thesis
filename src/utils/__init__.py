"""
Utility modules for logging and database connectivity.
"""
from .logger import setup_logger
from .excel_styling import (
    parse_cell_value,
    auto_fit_columns,
    autofit_column_widths,
    setup_return_link,
    apply_apa_table_borders,
    style_table_range,
    APA_FONT_NAME,
    BORDER_TOP_BOTTOM,
    BORDER_BOTTOM_ONLY,
    BORDER_NONE,
    FONT_TABLE_ID,
    FONT_TABLE_TITLE,
    FONT_HEADER,
    FONT_DATA,
    FONT_NOTE,
    FONT_LINK,
)

__all__ = [
    "setup_logger",
    "parse_cell_value",
    "auto_fit_columns",
    "autofit_column_widths",
    "setup_return_link",
    "apply_apa_table_borders",
    "style_table_range",
    "APA_FONT_NAME",
    "BORDER_TOP_BOTTOM",
    "BORDER_BOTTOM_ONLY",
    "BORDER_NONE",
    "FONT_TABLE_ID",
    "FONT_TABLE_TITLE",
    "FONT_HEADER",
    "FONT_DATA",
    "FONT_NOTE",
    "FONT_LINK",
]

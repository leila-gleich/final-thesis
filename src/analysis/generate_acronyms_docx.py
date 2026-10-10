"""
generate_acronyms_docx.py (src/analysis wrapper)
================================================
Proxy module forwarding directly to src/manuscripts/generate_acronyms_docx.py
to maintain backward compatibility across all analytical and manuscript scripts.
"""

from src.manuscripts.generate_acronyms_docx import (
    ACRONYM_DATA,
    CATEGORIES,
    sort_key,
    set_cell_margins,
    apply_apa_table_borders,
    build_word_document,
    build_markdown_document,
    main
)

if __name__ == "__main__":
    main()

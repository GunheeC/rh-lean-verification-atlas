"""PDF fragment pages are counted from the cover, independently of printed folios."""


def blueprint_page(edition, v13_physical):
    """Map an existing physical sheet, including v13's own preliminaries."""
    if not 1 <= v13_physical <= edition["retained_v13_pages"]:
        raise ValueError(f"Unknown blueprint v13 PDF page {v13_physical}")
    return edition["new_front_pages"] + v13_physical


def packet_page_links(edition, packet):
    path = "../" + edition["repository_file"]
    return " · ".join(
        f"[{folio}]({path}#page={blueprint_page(edition, physical)})"
        for folio, physical in zip(packet["printed_pages"], packet["pdf_pages"], strict=True)
    )

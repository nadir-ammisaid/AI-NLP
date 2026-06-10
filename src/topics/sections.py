# Diviser les paragraphes en N sections égales (N = 3 par défaut) si pas de chapitres trouvés
def split_into_sections(
    paragraphs,
    section_count=3,
):
    size = len(paragraphs) // section_count
    sections = []

    for i in range(section_count):
        start = i * size
        if i == section_count - 1:
            end = len(paragraphs)
        else:
            end = (i + 1) * size
        sections.append(paragraphs[start:end])

    return sections

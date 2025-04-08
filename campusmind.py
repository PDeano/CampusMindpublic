import os

# Default study materials based on common school subjects
MATERIAL_LIST = [
    ("Mathematics", "Numbers, shapes, patterns: algebra, geometry, calculus, statistics."),
    ("English Language Arts", "Reading, writing, literature, grammar, composition, text analysis."),
    ("Biology", "Study of living organisms: cells, genetics, evolution, ecology."),
    ("Chemistry", "Matter and its interactions: atoms, reactions, stoichiometry, thermodynamics."),
    ("Physics", "Principles of energy and motion: mechanics, waves, electricity, magnetism."),
    ("History", "Past events and societies: ancient to modern world history."),
    ("Geography", "Earth’s features and human-environment interactions: physical and human geography."),
    ("Civics & Government", "Citizenship, political systems, rights, and responsibilities."),
    ("Economics", "Resource allocation, markets, supply and demand, personal finance."),
    ("Foreign Languages", "Spanish, French, Mandarin, etc.: speaking, listening, reading, writing."),
    ("Health & PE", "Physical fitness, nutrition, wellness, team sports."),
    ("Visual Arts", "Drawing, painting, sculpture, art history, design principles."),
    ("Music", "Theory, performance, history, composition."),
    ("Drama", "Acting, directing, stagecraft, script analysis."),
    ("Computer Science", "Computing fundamentals, programming, digital literacy, online safety."),
    ("Business Studies", "Accounting, marketing, management, entrepreneurship."),
    ("Family & Consumer Science", "Life skills: cooking, budgeting, child development."),
    ("Psychology", "Behavior, cognition, development, mental health basics."),
    ("Environmental Science", "Ecosystems, sustainability, conservation, human impact."),
]
DEFAULT_MATERIALS = dict(MATERIAL_LIST)

def load_materials(file_path="materials.txt"):
    """
    Load study materials from a text file into a dictionary.
    Each line: Title::Content
    Falls back to DEFAULT_MATERIALS if file missing or empty.
    """
    materials = DEFAULT_MATERIALS.copy()
    if not os.path.exists(file_path):
        print(f"Note: {file_path} not found. Using default materials.")
        return materials

    loaded = False
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            if '::' in (l := line.strip()):
                title, content = l.split('::', 1)
                materials[title.strip()] = content.strip()
                loaded = True
    if not loaded:
        print(f"Note: {file_path} empty or invalid. Using default materials.")
    return materials


def search_materials(materials, keyword):
    kw = keyword.lower()
    return {t: c for t, c in materials.items() if kw in t.lower() or kw in c.lower()}


def display_materials(results):
    if not results:
        print("No matching materials found.")
        return
    print(f"Found {len(results)} material(s):\n")
    for i, (t, c) in enumerate(results.items(), 1):
        print(f"{i}. {t}\n   {c}\n")


def main():
    print("Welcome to CampusMind: Digital Study Material Finder")
    mats = load_materials()
    while True:
        kw = input("\nEnter keyword (or 'exit'): ").strip()
        if kw.lower() == 'exit':
            print("Goodbye!")
            break
        display_materials(search_materials(mats, kw))


if __name__ == '__main__':
    main()
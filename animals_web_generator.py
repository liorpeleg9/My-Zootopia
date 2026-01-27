import data_fetcher

TEMPLATE_FILE = "animals_template.html"
OUTPUT_FILE = "animals.html"


def serialize_animal(animal: dict) -> str:
    parts = []
    parts.append('<li class="cards__item">')

    name = animal.get("name")
    if name:
        parts.append(f'<div class="card__title">{name}</div>')

    parts.append('<p class="card__text">')

    characteristics = animal.get("characteristics") or {}

    diet = characteristics.get("diet")
    if diet:
        parts.append(f"<strong>Diet:</strong> {diet}<br/>")

    locations = animal.get("locations") or []
    if locations:
        parts.append(f"<strong>Location:</strong> {locations[0]}<br/>")

    animal_type = characteristics.get("type")
    if animal_type:
        parts.append(f"<strong>Type:</strong> {animal_type}<br/>")

    parts.append("</p>")
    parts.append("</li>")

    return "\n".join(parts)


def build_animals_info(animals: list) -> str:
    return "\n".join(serialize_animal(a) for a in animals) + ("\n" if animals else "")


def build_not_found_message(animal_name: str) -> str:
    safe = animal_name.replace('"', "&quot;")
    return f'<h2>The animal "{safe}" doesn\'t exist.</h2>'


def generate_html(content_html: str) -> None:
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", content_html)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final_html)


def main():
    animal_name = input("Enter a name of an animal: ").strip()

    animals = data_fetcher.fetch_data(animal_name)

    if animals:
        animals_html = build_animals_info(animals)
    else:
        animals_html = build_not_found_message(animal_name)

    generate_html(animals_html)
    print(f"Website was successfully generated to the file {OUTPUT_FILE}.")


if __name__ == "__main__":
    main()

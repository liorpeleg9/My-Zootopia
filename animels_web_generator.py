import json


def load_data(file_path):
    """Load and return JSON data from animals_data.json."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """Convert one animal dictionary into one HTML <li> card string."""
    parts = []
    parts.append('<li class="cards__item">')

    name = animal.get("name")
    if name:
        parts.append(f'<div class="card__title">{name}</div>')

    parts.append('<p class="card__text">')

    characteristics = animal.get("characteristics", {})

    diet = characteristics.get("diet")
    if diet:
        parts.append(f"<strong>Diet:</strong> {diet}<br/>")

    locations = animal.get("locations", [])
    if locations:
        parts.append(f"<strong>Location:</strong> {locations[0]}<br/>")

    animal_type = characteristics.get("type")
    if animal_type:
        parts.append(f"<strong>Type:</strong> {animal_type}<br/>")

    parts.append("</p>")
    parts.append("</li>")

    return "\n".join(parts)



def build_animals_info(data):
    """Building one HTML string that contains all the animal cards."""
    animals_info = ""
    for animal in data:
        animals_info += serialize_animal(animal) + "\n"
    return animals_info


def main():
    data = load_data("animals_data.json")

    animals_info = build_animals_info(data)

    with open("animals_template.html", "r", encoding="utf-8") as f:
        template = f.read()

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open("animals.html", "w", encoding="utf-8") as f:
        f.write(final_html)


if __name__ == "__main__":
    main()

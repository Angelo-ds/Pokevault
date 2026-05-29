import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed


def get_pokemon_data(pokemon_id):

    pokemon = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    ).json()

    species = requests.get(
        f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}"
    ).json()

    description = ""

    for entry in species["flavor_text_entries"]:
        if entry["language"]["name"] == "en":
            description = entry["flavor_text"].replace("\n", " ").replace("\f", " ")
            break

    return {
        "id": pokemon["id"],
        "name": pokemon["name"],
        "types": [t["type"]["name"] for t in pokemon["types"]],
        "image": pokemon["sprites"]["other"]["official-artwork"]["front_default"],
        "description": description
    }


def fetch(pokemon_id):
    try:
        data = get_pokemon_data(pokemon_id)

        # PRINT ASSIM QUE TERMINAR
        print(f"✔ {data['id']} - {data['name']} carregado")

        return data

    except Exception as e:
        print(f"✖ erro no {pokemon_id}")
        return None


all_pokemons = []


with ThreadPoolExecutor(max_workers=10) as executor:

    futures = [executor.submit(fetch, i) for i in range(1, 387)]

    for future in as_completed(futures):

        result = future.result()

        if result:
            all_pokemons.append(result)


with open("pokemons.json", "w", encoding="utf-8") as f:
    json.dump(all_pokemons, f, ensure_ascii=False, indent=4)


print("🔥 Finalizado! JSON criado.")
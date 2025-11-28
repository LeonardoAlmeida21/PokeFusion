import csv
from pathlib import Path


def build_prompt(name: str, primary: str, secondary: str | None) -> str:
    normalized_name = name.replace("-", " ").replace("_", " ")
    parts = ["pixel_art style", normalized_name]
    if primary:
        parts.append(f"{primary} type")
    if secondary:
        parts.append(f"{secondary} type")
    return ", ".join(parts)


def main() -> None:
    base_dir = Path(__file__).parent
    csv_path = base_dir / "dataset" / "pokemon_full.csv"
    out_dir = base_dir / "outputs_txt"
    out_dir.mkdir(exist_ok=True)

    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["english_name"]
            primary = (row.get("primary_type") or "").strip()
            secondary = (row.get("secondary_type") or "").strip()
            secondary = secondary if secondary else None

            prompt = build_prompt(name, primary, secondary)
            (out_dir / f"{name}.txt").write_text(prompt, encoding="utf-8")


if __name__ == "__main__":
    main()

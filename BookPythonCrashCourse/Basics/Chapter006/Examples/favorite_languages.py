favorite_languages: dict[str, str] = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
}

print(f"{favorite_languages}\n")

favorite_language: str = favorite_languages.get("diego")
print(favorite_language)

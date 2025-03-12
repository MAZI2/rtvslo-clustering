import yaml


def load_articles():
    return yaml.load(open("articles.yaml", "r", encoding="utf-8"), Loader=yaml.CFullLoader)


if __name__ == "__main__":
    # Tukaj naj se ustvarijo končni rezultati
    # ...

    articles = load_articles()

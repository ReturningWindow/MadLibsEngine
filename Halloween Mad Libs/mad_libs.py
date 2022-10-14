from mad_libs_handler import MadLibsHandler

games = [
    MadLibsHandler(
        "I can't believe it's Halloween",
        "I can't believe it's already {}! I can't wait to put on my {} and visit every {} in my neighborhood. This year, I am going to dress up as a {} with {} {}. Before I {}, I make sure to grab my {} {} to hold all of my {}. Finally, all of my {} are ready to go!",
        [
            "holiday",
            "noun",
            "place",
            "person",
            "adjective",
            "plural body part",
            "verb",
            "adjective",
            "noun",
            "noun",
            "food",
            "plural noun",
        ],
    ),
    MadLibsHandler(
        "Halloween is my favorite",
        "Halloween is my favorite, because we get to dress up in {} and visit {} in our {} saying \"{} or {}\"! In exchange for a bag of {}. It's so {}! This year, I'm going to dress up as a(n) {} {} my costume is going to be so {}! It will be made with {} {} and {}, so it's sure to win the {} {} contest! I also love to {} {} for Halloween! I use special carving {} to {} {} a face into my {} then, we put a {} inside and light it so that the {} {}! Spooky!",
        [
            "nouns",
            "nouns",
            "noun",
            "noun",
            "noun",
            "nouns",
            "adjective",
            "adjective",
            "noun",
            "adjective",
            "adjective",
            "nouns",
            "nouns",
            "adjective",
            "noun",
            "verb",
            "nouns",
            "nouns",
            "adverb",
            "verb",
            "noun",
            "noun",
            "noun",
            "verb that ends in s",
        ],
    ),
]


def main():
    for index, count in enumerate(games):
        print(f"{index+1}) {games[index].name}")

    while True:
        selection = input("Enter one of the choices above: ")
        if selection.isdigit():
            selection = int(selection)
            if selection <= 2:
                break

    games[selection - 1].play_mad_libs()
    print(games[selection - 1].get_mad_libs())


if __name__ == "__main__":
    main()

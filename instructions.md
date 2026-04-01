🧑‍💻 Osoba A: Architekt bludiště (Backend a logika)

Tato role se zaměří na algoritmy, zpracování dat a splnění základních technických požadavků.

    Bude mít na starosti načítání a parsování konfiguračního souboru (config.txt).

    Musí zajistit ošetření všech chyb (např. neplatná konfigurace nebo špatná syntaxe), aby program nikdy neočekávaně nespadl.

    Naimplementuje samotný algoritmus pro generování bludiště, přičemž musí zajistit, aby bylo generování náhodné, ale reprodukovatelné pomocí seedu.

    Zajistí, aby struktura bludiště byla platná, obsahovala vstup a výstup na vnějších hranicích a neměla izolované buňky.

    Implementuje logiku pro vytvoření "perfektního" bludiště (s jedinou možnou cestou), pokud je v konfiguraci aktivován příznak PERFECT.

    Vytvoří funkci pro zápis vygenerovaného bludiště do výstupního souboru pomocí hexadecimálních číslic, kde každý bit kóduje přítomnost stěny.

🎨 Osoba B: Vizualizátor a integrátor (Frontend a balíčkování)

Tato role se zaměří na to, jak bludiště vypadá, jak s ním uživatel komunikuje a jak je projekt zabalen pro další použití.

    Vytvoří vizuální reprezentaci bludiště buď pomocí ASCII v terminálu, nebo graficky pomocí knihovny MiniLibX (MLX).

    Vizuál musí jasně zobrazovat stěny, vstup, výstup a cestu řešení.

    Naprogramuje uživatelské interakce, konkrétně možnost přegenerovat bludiště, skrýt/zobrazit nejkratší cestu a změnit barvy stěn.

    Zajistí (ve spolupráci s Osobou A), aby vizuální reprezentace obsahovala viditelný vzor "42", který je tvořen plně uzavřenými buňkami.

    Zabalí generátor bludiště jako samostatný, znovupoužitelný modul ve formátu instalovatelném přes pip (s názvem mazegen-*).

🤝 Společné úkoly (Doporučuji dělat formou párového programování)

Některé části projektu vyžadují shodu obou členů týmu a úzkou spolupráci.

    Vytvoření souboru Makefile pro automatizaci úkolů s pravidly install, run, debug, clean a lint.

    Kontrola kódu: zajištění, že celý projekt je napsán v Pythonu 3.10+, splňuje standard flake8 a obsahuje typové nápovědy kontrolované nástrojem mypy.

    Sepsání kvalitního dokumentu README.md, který musí obsahovat popis projektu, použité algoritmy a také rozdělení rolí a řízení projektu v rámci vašeho týmu.
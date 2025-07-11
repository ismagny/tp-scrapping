# utilise le code suivant pour stocker dans un fichier txt
# les informations title, instructions, ingredients et nutrients
# de chaque recette de cuisine présente dans la liste des urls
# PS recipe_scrapers vient de https://github.com/hhursev/recipe-scrapers
import json
import os

# crée ensuite un script de lecture du fichier
# et une classe Recipe
# qui représente une recette extraite d'une url

# PS : commence ton TP avec une ou deux urls pour ensuite faire le processus sur les 100 urls présentes

from recipe_scrapers import scrape_me

urls = ['https://www.allrecipes.com/recipe/21014/good-old-fashioned-pancakes/'
    , 'https://www.allrecipes.com/recipe/22162/uglies/', 'https://www.allrecipes.com/recipe/140286/homemade-dog-food/',
        'https://www.allrecipes.com/the-10-minute-recipe-i-make-once-a-week-11742451',
        'https://www.allrecipes.com/recipe/16248/easy-homemade-chili/',
        'https://www.allrecipes.com/recipe/16383/basic-crepes/',
        'https://www.allrecipes.com/recipe/234933/how-to-make-perfect-polenta/',
        'https://www.allrecipes.com/recipe/58942/absolute-best-liver-and-onions/',
        'https://www.allrecipes.com/recipe/7177/bread-pudding-ii/',
        'https://www.allrecipes.com/recipe/51301/sarahs-applesauce/',
        'https://www.allrecipes.com/recipe/9870/easy-sugar-cookies/',
        'https://www.allrecipes.com/recipe/17481/simple-white-cake/',
        'https://www.allrecipes.com/recipe/228774/emergency-chicken/',
        'https://www.allrecipes.com/recipe/223042/chicken-parmesan/',
        'https://www.allrecipes.com/recipe/6761/tasty-buns/', 'https://www.allrecipes.com/recipe/35149/corn-dogs/',
        'https://www.allrecipes.com/recipe/11867/death-by-garlic/',
        'https://www.allrecipes.com/recipe/71484/i-dont-know/', 'https://www.allrecipes.com/recipe/24448/my-favorites/',
        'https://www.allrecipes.com/recipe/20586/homemade-vanilla-pudding/',
        'https://www.allrecipes.com/recipe/11899/basic-pasta/',
        'https://www.allrecipes.com/recipe/222006/disneys-ratatouille/',
        'https://www.allrecipes.com/recipe/222352/jamies-sweet-and-easy-corn-on-the-cob/',
        'https://www.allrecipes.com/red-white-and-blue-cheesecake-bites-recipe-7554460',
        'https://www.allrecipes.com/recipe/21006/fried-cornmeal-mush/',
        'https://www.allrecipes.com/recipe/85129/fleischkuechle-flesh-keek-luh/',
        'https://www.allrecipes.com/recipe/221972/chef-johns-cioppino/',
        'https://www.allrecipes.com/recipe/15983/grannys-cherokee-casserole/',
        'https://www.allrecipes.com/recipe/30918/irish-boiled-dinner-corned-beef/',
        'https://www.allrecipes.com/recipe/269742/soul-food-seasoning/',
        'https://www.allrecipes.com/recipe/10857/dishpan-cookies-i/',
        'https://www.allrecipes.com/recipe/233122/perfect-fried-green-tomatoes/',
        'https://www.allrecipes.com/garlic-butter-grilled-cheese-hotdog-recipe-11763786',
        'https://www.allrecipes.com/recipe/218619/easy-bok-choy/',
        'https://www.allrecipes.com/recipe/229290/homemade-baking-powder-recipe/',
        'https://www.allrecipes.com/italian-penicillin-soup-recipe-8751324',
        'https://www.allrecipes.com/recipe/17072/thirty-minute-meal/',
        'https://www.allrecipes.com/recipe/242401/homemade-worcestershire-sauce/',
        'https://www.allrecipes.com/recipe/139453/lucky-and-rippys-favorite-dog-food/',
        'https://www.allrecipes.com/easy-summer-dump-cake-recipe-11759738',
        'https://www.allrecipes.com/recipe/285393/bialys/', 'https://www.allrecipes.com/recipe/16304/husbands-delight/',
        'https://www.allrecipes.com/recipe/146125/chicken-julienne/',
        'https://www.allrecipes.com/recipe/17891/golden-sweet-cornbread/',
        'https://www.allrecipes.com/father-in-law-favorite-shrimp-recipe-11748331',
        'https://www.allrecipes.com/recipe/57176/gunk-on-noodles/',
        'https://www.allrecipes.com/recipe/14415/cobb-salad/',
        'https://www.allrecipes.com/recipe/11352/three-ingredient-peanut-butter-cookies/',
        'https://www.allrecipes.com/recipe/257242/norwegian-butter-sauce-sandefjordsmor/',
        'https://www.allrecipes.com/recipe/34450/italian-seasoning-i/',
        'https://www.allrecipes.com/recipe/213015/daves-georgia-black-eyed-peas/',
        'https://www.allrecipes.com/recipe/81942/new-york-knish-yo/',
        'https://www.allrecipes.com/recipe/53683/perfect-lemon-curd/',
        'https://www.allrecipes.com/recipe/222000/spaghetti-aglio-e-olio/',
        'https://www.allrecipes.com/recipe/13961/baked-vegetables-i/',
        'https://www.allrecipes.com/recipe/8380474/dynamite-rice/',
        'https://www.allrecipes.com/recipe/214931/oven-roasted-asparagus/',
        'https://www.allrecipes.com/recipe/228333/cuban-inspired-millet/',
        'https://www.allrecipes.com/recipe/228823/quick-beef-stir-fry/',
        'https://www.allrecipes.com/recipe/11758/baked-ziti-i/',
        'https://www.allrecipes.com/recipe/228755/braunschweiger-potato-hash/',
        'https://www.allrecipes.com/recipe/26159/kolachky/',
        'https://www.allrecipes.com/recipe/240206/simple-broccolini/',
        'https://www.allrecipes.com/recipe/238510/homemade-arepas/',
        'https://www.allrecipes.com/my-husbands-favorite-hot-dog-recipe-11764543',
        'https://www.allrecipes.com/recipe/221361/traditional-sauerbraten/',
        'https://www.allrecipes.com/recipe/83097/authentic-german-potato-salad/',
        'https://www.allrecipes.com/summer-barbecue-casserole-recipe-11748413',
        'https://www.allrecipes.com/recipe/228641/chef-johns-popovers/',
        'https://www.allrecipes.com/recipe/15432/angel-food-cake-iii/',
        'https://www.allrecipes.com/article/my-grandmas-chicken-wings-recipe/',
        'https://www.allrecipes.com/recipe/11713/the-cheese-thing/',
        'https://www.allrecipes.com/recipe/241074/easy-garlic-kale/',
        'https://www.allrecipes.com/recipe/14064/easy-guacamole/',
        'https://www.allrecipes.com/recipe/190276/easy-shakshuka/',
        'https://www.allrecipes.com/recipe/256888/chef-johns-pate-de-campagne/',
        'https://www.allrecipes.com/recipe/109810/italian-style-swiss-chard/',
        'https://www.allrecipes.com/recipe/24272/buttery-soft-pretzels/',
        'https://www.allrecipes.com/recipe/257961/neeps-and-tatties/',
        'https://www.allrecipes.com/recipe/258755/simple-custard/',
        'https://www.allrecipes.com/recipe/8909/chicken-and-rice/',
        'https://www.allrecipes.com/recipe/20487/old-fashioned-lemonade/',
        'https://www.allrecipes.com/recipe/24059/creamy-rice-pudding/',
        'https://www.allrecipes.com/recipe/259162/ratatouille-provencale/',
        'https://www.allrecipes.com/recipe/158140/spaghetti-sauce-with-ground-beef/',
        'https://www.allrecipes.com/recipe/10412/welsh-cookies/',
        'https://www.allrecipes.com/recipe/229870/thats-good-moosh/',
        'https://www.allrecipes.com/recipe/275183/homemade-grain-free-dog-food/',
        'https://www.allrecipes.com/recipe/22749/the-best-banana-pudding/',
        'https://www.allrecipes.com/recipe/46653/taco-seasoning-i/',
        'https://www.allrecipes.com/recipe/50223/homemade-crispy-seasoned-french-fries/',
        'https://www.allrecipes.com/recipe/164920/easy-dinner-hash/',
        'https://www.allrecipes.com/recipe/11215/benne-wafers/',
        'https://www.allrecipes.com/recipe/223051/chef-johns-colcannon/',
        'https://www.allrecipes.com/recipe/24332/ultimate-twice-baked-potatoes/',
        'https://www.allrecipes.com/recipe/216159/perfect-chicken/',
        'https://www.allrecipes.com/recipe/258879/kewa-datshi-bhutanese-dish/',
        'https://www.allrecipes.com/recipe/10402/the-best-rolled-sugar-cookies/',
        'https://www.allrecipes.com/tang-pie-recipe-11759885']

def recipe_write(url, i_rec):
    try:
        scraper = scrape_me(url)
        titre = scraper.title()
        instructions = scraper.instructions()
        ingredients = scraper.ingredients()
        nutrients = scraper.nutrients()

        recette_json = {
            "recette": i_rec,
            "titre": titre,
            "instructions": instructions,
            "ingredients": ingredients,
            "nutriments": nutrients
        }

        # Lire le fichier existant ou créer une liste vide
        if os.path.exists("recipes.json"):
            with open("recipes.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = []

        # Ajouter la recette et réécrire le fichier complet
        data.append(recette_json)

        with open("recipes.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    except Exception as e:
        print(f"❌  Erreur sur {url} : {e}")

def recipe_scrapper():
    for i_rec, url in enumerate(urls, 1):
        recipe_write(url, i_rec)

recipe_scrapper()
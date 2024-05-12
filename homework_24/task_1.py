import json


def where_to_buy(ingredients, markets):
    result = dict()
    for market, products in markets.items():
        if ingredients & set(products):
            result[market] = list(ingredients & set(products))
            ingredients -= set(products)
    if not ingredients:
        return result


def readout(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(F"Can't open {filename} file.")


def main():
    recipes = readout("recipes.json")
    markets = readout("markets.json")
    list_recipes = list(recipes)

    for i in range(len(recipes)):
        print(F"{i+1}. {list_recipes[i]}")
    index = int(input("Choose a recipe: "))-1

    try:
        recipe = list_recipes[index]
    except IndexError:
        print("You entered invalid number.")
        exit(-1)

    ingredients = set(recipes[recipe]["ingredients"])
    print(F"\nIngredients for {recipe}: {ingredients}")
    result = where_to_buy(ingredients, markets)

    if result:
        print("Where to buy products:")
        for market, products in result.items():
            print(F"\t{market}: ", end='')
            for i in products:
                print(F"{i}", end='')
                if i != products[-1]:
                    print(", ", end='')
                else:
                    print()
    else:
        print("There is no ingredients in markets!")


if __name__ == '__main__':
    main()

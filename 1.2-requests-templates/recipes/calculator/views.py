from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)


        'ratatouille': {
        'цуккини, гр': 130,
        'баклажаны, гр': 130,
        'томаты, гр': 90,
        'лук, гр': 20,
        'соль, гр': 2,
        'перец, гр': 3,
        'базилик, гр': 10,
        'масло оливковое, мл': 20,
    },
    'pasta parmijano': {
        'спагетти, гр': 70,
        'сыр, гр': 0.1,
        'пармская ветчина, гр': 50,
        'сливки, гр': 20,
        'яйца, шт': 1,
        'лук, гр': 20,
        'соль, гр': 2,
        'перец, гр': 3,
        'базилик, гр': 10,
        'масло оливковое, мл': 20,
    },

}


def get_recipe(request, dish):
    servings = int(request.GET.get('servings', 1))
    ingredients = DATA.get(dish).copy()

    for key in ingredients:
        ingredients[key] = DATA.get(dish)[key] * servings

    context = {
        'recipe': ingredients,
        'servings': servings
    }

    return render(request, 'calculator/index.html', context)
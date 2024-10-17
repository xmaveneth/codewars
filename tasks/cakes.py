def cakes(recipe, available):
    data = []
    for i in recipe:
        if i not in available:
            return 0
        data.append(available[i] // recipe[i])
    return min(data)


# https://www.codewars.com/kata/525c65e51bf619685c000059


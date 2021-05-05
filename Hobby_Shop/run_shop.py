# hobby shop
import random

types_of_articles = ["blazer", "dress", "shirt", "top", "jean",
                     "jacket", "skirt", "coat", "suit"]
sizes = ["XS", "S", "M", "L", "XL"]
my_shop = [[], []]


def verify_product(article_name, article_size):
    if article_name in types_of_articles:
        if article_size in sizes:
            return True
        else:
            print("We don't carry that size, item not added to stock")
            return False
    else:
        print("We don't sell that type of article, item not added to stock")
        return False


def add_to_shop(art_type, art_size):
    if verify_product(art_type, art_size):
        my_shop[0].append(art_type)
        my_shop[1].append(art_size)


def sell_last_added_item():
    my_shop[0].pop()
    my_shop[1].pop()


def sell_specific_item(article, size):
    if verify_product(article, size):
        for i in range(len(my_shop[0])):
            if my_shop[0][i] == article:
                if my_shop[1][i] == size:
                    my_shop[0].pop(i)
                    my_shop[1].pop(i)
                    print(i)
                    break


def generate_shop_stock():
    articles_stock = []
    sizes_stock = []
    products_in_stock = 500

    for i in range(products_in_stock):
        rand_article_index = random.randint(0, 8)
        rand_size_index = random.randint(0, 4)

        temp_article = types_of_articles[rand_article_index]
        temp_size = sizes[rand_size_index]

        articles_stock.append(temp_article)
        sizes_stock.append(temp_size)
    my_shop[0] = articles_stock
    my_shop[1] = sizes_stock


def __main__():
    generate_shop_stock()
    add_to_shop("blazer", "M")
    add_to_shop("jean", "S")
    add_to_shop("coat", "S")
    sell_last_added_item()
    sell_specific_item("coat", "S")
    sell_specific_item("blug", "M")


__main__()

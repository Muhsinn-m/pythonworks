#construct a product details (id=369,tittle=cooldrink,price=29,brand=itc)

product={"id":369,"title":"cool drink","price":29,"brand":"itc"}

print(product["price"])


#update product price as 50

product["price"]=50

print(product)


# pdate brand name to coca cola

product["brand"]="coca cola"

print(product)


#update product "offer=5"

product["offer"]=5

print(product)


#add offer as 10 if offer exist else add offer  as 20

if "offer" in product:

    product["offer"]=10

else:
    product["offer"]=20

print(product)
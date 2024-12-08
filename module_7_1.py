
class Product:
    def __init__(self, name:str, weight:float, category:str):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'a') #создание файла, если ещё не было
        file.close()
    def get_products(self):
        file = open(self.__file_name, 'r')
        str_products = file.read()
        file.close()
        return str_products
    def add(self, *products:Product):
        str_products = self.get_products()
        set_products = set()
        pos = 0
        start_pos = 0
        while pos < len(str_products):
            if str_products[pos] == '\n':
                start_pos = pos + 1
            elif str_products[pos] == ',' and start_pos != -1:
                set_products.add(str_products[start_pos:pos])
                start_pos = -1
            pos += 1

        file = open(self.__file_name, 'a')
        for prod in products:
            if prod.name in set_products:
                print(f'Продукт {prod.name} уже есть в магазине')
            else:
                file.write(str(prod)+'\n')


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    print(p2)  # __str__
    s1.add(p1, p2, p3)
    print(s1.get_products())


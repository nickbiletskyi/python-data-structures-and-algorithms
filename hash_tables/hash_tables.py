
class HashTables:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])


    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for item in self.data_map[index]:
                if item[0] == key:
                    return item[1]
        return

    # def keys(self):
    #     hey = [[item_1[0] for item_1 in item] for item in self.data_map if item]
    #     return hey

    def keys(self):
        keys = []
        for items in self.data_map:
            if items:
                for item in items:
                    keys.append(item[0])

        return keys








my_hash_table = HashTables()
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
print(my_hash_table.get_item('lumbers'))
print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('washers'))

print(my_hash_table.keys())
my_hash_table.print_table()

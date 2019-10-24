class Level_map():
    def __init__(self):
        self.map_file = None
        self.map_generator()

    def get_env(self, pos):
        pass

    def map_generator(self, x_size, y_size):
        """
        Map consists of chunks (8x8 cells)
        Every chunk is a sequence of 64 numbers - every number is a cell
        Chunks stored in string of 8 chunks
        """
        self.map_file = open("map.dat", 'w')
        for i in range(y_size):
            for j in range(x_size):
                self.map_file.write()
        # Generating map
        # One integer = 8 horisontal cells (ex: 0000 0000 0000 0000 0000 0000 0000 0000)


        # Карта будет состоять из чанков по 64 ячейки в каждом, генерация нового чанка будет происходить, учитывая дургие чанки
        # При генерации чанка просматриваем ближайшие и делаем соответствующий выводы
        # Чанк будет хранится как последовательность из 64 чисел в одну строку a00, a01, ..., a0n, a10, a11, ... , ann
        # Разделителем будет знак табуляции
        # Новая строка чанков будет находиться в следующей строке
        # Быть может с этим заморачиваться не стоит
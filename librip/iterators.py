# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, ignore_case = False):
        self.list = self.GetUniqueList(items, ignore_case)
        self.iteration = -1

    def GetUniqueList(self, items, ignore_case):
        uniqueLst = []
        if ignore_case:
            itemsLower = []
            for item in items:
                itemsLower.append(str(item).lower())
            items = itemsLower
        for item in items:
            if item in uniqueLst:
                continue
            else:
                uniqueLst.append(item)
        return uniqueLst

    def __next__(self):
        self.iteration += 1
        if self.iteration < len(self.list):
            return self.list[self.iteration]
        else:
            raise StopIteration

    def __iter__(self):
        return self

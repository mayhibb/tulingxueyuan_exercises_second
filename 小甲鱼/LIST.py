class CountList:
    def __init__(self,*args):
        self.values = list(v for v in args)
        self.count = {}.fromkeys(self.values,0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self,key):
        self.count[key] += 1
        return self.values[key]

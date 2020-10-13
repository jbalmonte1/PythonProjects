from json import load
from os import listdir, path

class map(dict):
    __getattr__ = dict.__getitem__

    def __init__(self, d):
        self.update(**dict((k, self.parse(v))
                           for k, v in d.items()))

    @classmethod
    def parse(cls, v):
        if isinstance(v, dict):
            return cls(v)
        elif isinstance(v, list):
            return [cls.parse(i) for i in v]
        else:
            return v

def JsonMapper(module):
    dirpath = path.join(path.dirname(__file__), module)
    files = listdir(dirpath)
    mapping = {}
    for file in files:
        if ".json" in file:
           mapping[file.replace(".json", "")] = load(open(path.join(dirpath, file)))
    return map(mapping)

testAutomationPracticeBlogspot = JsonMapper("testautomationpractice.blogspot.com")
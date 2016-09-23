class LazyRules:
 #   rules_filename = 'E:\\books_and_materials\\Programming_Languages\\python\\dive-into-python-3-source-code\\chapter7\\plural6_rules.txt'
    rules_filename = 'plural6_rules.txt'

    def __init__(self):
        self.pattern_file = open(self.rules_filename,encoding = 'utf-8')
        self.cache=[]

    def __iter__(self):
        self.cache_index = 0
        return self

    def __next__(self):
        self.cache_index += 1
        if len(self.cache)>= self.cache_index:
            return self.cache[self.cache_index-1]

        if self.pattern_file.closed:
            raise StopIteration

        line = self.pattern_file.readline()
        if not line:
            self.pattern_file_close()
            raise StopIteration
        

        pattern,search,replace = line.split(None,2)
        funcs = build_match_and_apply_function(pattern,search,replace)
        self.cache.append(funcs)
        return funcs

rules = LazyRules()

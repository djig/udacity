class RouteTrieNode:
    def __init__(self, description, is_final_handler: False):
        self.children = dict()
        self.description = description
        self.is_final_handler = is_final_handler
class RouteTrie:
    def __init__(self, description, is_final_handler):
        self.root = RouteTrieNode(description, is_final_handler)

    def insert(self, paths,description):
        curr = self.root
        for path in paths:
            if not path in curr.children:
                curr.children[path] = RouteTrieNode('', False)
            curr = curr.children[path]
        curr.description = description
        curr.is_final_handler = True

class Router:
    def __init__(self, rootMessage, notFoundMessage):
        self.router = RouteTrie(rootMessage, False)
        self.rootMessage = rootMessage
        self.notFoundMessage = notFoundMessage
    def split_path(self, path):
        return path.split('/')[1:] 
    def add_handler(self, path, desc):
        paths = self.split_path(path)
        if len(paths) == 0 or len(desc) == 0:
            print(paths)
            print('Not Valid Handler or Path')
            return
        self.router.insert(paths, desc)
    def lookup(self, path):

        if path == '/':
            return self.rootMessage
        paths = self.split_path(path)
        curr = self.router.root
        for p in paths:
            if not p in curr.children:
                return self.notFoundMessage
            curr = curr.children[p]
        if curr.is_final_handler == True:
            return curr.description
        else:
            return self.notFoundMessage


router = Router("root handler", "not found handler") 
router.add_handler("/home/about", "about handler")
router.add_handler("/settings/admin", "admin handler")
router.add_handler("/product/list", "product list handler")
router.add_handler("/home/admin/nohandler", "")
router.add_handler("", "sasa")
print(router.lookup("/"))
print(router.lookup("/home"))
print(router.lookup("/home/about"))
print(router.lookup("/settings/admin"))
print(router.lookup("/product/"))
print(router.lookup("/product/list"))
print(router.lookup("dsds"))

import ast

# path = 'SampleIncludingAll1.py'
# tree = ast.parse(open(path).read())


class base_reader(ast.NodeVisitor):
    def __init__(self):
        self.base_name = ''

    def visit_ClassDef(self, node):
        if len(node.bases)==1:
            if isinstance(node.bases[0],ast.Name):
                self.base_name = node.bases[0].id

def get_keys(dic, value):
    return [k for k, v in dic.items() if v == value]
class NOC():

    def __init__(self, p):
        self.p_way = p
    def count_NOC(self):
        result = ''
        total_list={}
        class_Def_name=[]
        for node in ast.walk(ast.parse(open(self.p_way).read())):
            if isinstance(node, ast.ClassDef):
                class_Def_name.append(node.name)
                g = base_reader()
                g.visit(node)
                # if g.base_name!=''and g.base_name!='object':
                #     total_list2[node.name]=g.base_name
                if g.base_name!='':
                    total_list[node.name]=g.base_name

        for i in class_Def_name:
            result+= i+'='+str(len(get_keys(total_list,i)))+'\n'
        return result
# print(class_Def_name)
# print(total_list)
# print(get_keys(total_list,'NumberOfChildrenExample1'))
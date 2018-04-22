import ast
from collections import deque

path = 'SampleIncludingAll1.py'
tree = ast.parse(open(path).read())



class FunctionCallVisitor(ast.NodeVisitor):
    def __init__(self):
        self.attr_name = deque()

    @property
    def info(self):
        return '.'.join(self.attr_name)

    def visit_Name(self, node):
        if self.attr_name != deque():
            self.attr_name.appendleft(node.id)

    def visit_Attribute(self, node):

        self.attr_name.appendleft(node.attr)
        self.generic_visit(node)



# total_list=[]
class CBO():
    def __init__(self,p):
        self.p_way=p
    def count_CBO(self):
        result=''
        for node in ast.walk(ast.parse(open(self.p_way).read())):
            if isinstance(node, ast.ClassDef):
                class_def_list = []
                # class_def_list.append(node.name)
                varDict = {}
                coupling_list = []
                for functions in node.body:
                    if isinstance(functions, ast.FunctionDef):
                        for statement in functions.body:
                            a = FunctionCallVisitor()
                            a.visit(statement)
                            if functions.name == '__init__' and not a.info.startswith('self.') and a.info != '':
                                temp = a.info.split('.')
                                varDict[temp[2]] = temp[0]
                            elif a.info != '':
                                class_def_list.append(a.info)

                count=0
                for attr in class_def_list:
                    temp = attr.split('.')
                    if temp[0] != 'self':
                        coupling_list.append(temp[0])
                    if varDict != {}:
                        for key, value in varDict.items():
                            if key in temp:
                                coupling_list.append(value)
                                count=len(coupling_list)


                result+=node.name + '<-> ' + str(coupling_list) + '= ' + str(count)+'\n'

        return result




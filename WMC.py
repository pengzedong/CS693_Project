import ast

path = 'SampleIncludingAll1.py'
tree = ast.parse(open(path).read())
class WMC():
    def __init__(self,p):
        self.p_way=p
    def count_WMC_off(self):
        result=''
        main_list = []
        for node in ast.walk(ast.parse(open(self.p_way).read())):
            if isinstance(node, ast.ClassDef):
                ClassDef_list = []
                ClassDef_list.append(node.name)
                for statement in node.body:
                    if isinstance(statement, ast.FunctionDef):
                        FunctionDef_list = []
                        if statement.name != '__init__':
                            FunctionDef_list.append(statement.name)
                            ClassDef_list.append(FunctionDef_list)
                main_list.append(ClassDef_list)

        name_list = []
        for node in ast.walk(ast.parse(open(self.p_way).read())):
            if isinstance(node, ast.ClassDef):
                name_list.append(node.name)

        # WMC (constructor=OFF)

        for i in range(len(name_list)):
            result+=name_list[i]+ '='+str( len(main_list[i]) - 1)+'\n'
        return result
        # WMC (constructor=on)


    def count_WMC_on(self):
        result=''
        main_list = []
        for node in ast.walk(ast.parse(open(self.p_way).read())):
            if isinstance(node, ast.ClassDef):
                ClassDef_list = []
                ClassDef_list.append(node.name)
                for statement in node.body:
                    if isinstance(statement, ast.FunctionDef):
                        FunctionDef_list = []
                        FunctionDef_list.append(statement.name)
                        ClassDef_list.append(FunctionDef_list)
                main_list.append(ClassDef_list)

        name_list = []
        for node in ast.walk(ast.parse(open(self.p_way).read())):
            if isinstance(node, ast.ClassDef):
                name_list.append(node.name)

        for i in range(len(name_list)):
            result += name_list[i] + '=' + str(len(main_list[i]) - 1) + '\n'
        return result

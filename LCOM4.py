import ast

# path = 'sample2.py'
# path = 'SampleIncludingAll1.py'
# tree = ast.parse(open(path).read())



class attr_reader(ast.NodeVisitor):
    def __init__(self):
        self.attr_name = ''

    def visit_Attribute(self, node):
        self.attr_name = node.attr

class LOCM4():
    def __init__(self,p):
        self.p_way=p

    def count_LOCM(self):
        main_list = []
        result=''
        for node in ast.walk(ast.parse(open(self.p_way).read())):
            if isinstance(node, ast.ClassDef):
                ClassDef_list = []
                # ClassDef_list.append(node.name)
                for statement in node.body:
                    if isinstance(statement, ast.FunctionDef):
                        FunctionDef_list = []
                        if statement.name != '__init__':
                            FunctionDef_list.append(statement.name)
                            for Assign in statement.body:
                                visitor = attr_reader()
                                visitor.visit(Assign)
                                if visitor.attr_name != '__init__':
                                    if visitor.attr_name != '':
                                        FunctionDef_list.append(visitor.attr_name)
                            ClassDef_list.append(FunctionDef_list)
                main_list.append(ClassDef_list)
        #print(main_list)


        def find_key(v, a):
            for key, value in v.items():
                # print(value)
                if a in value:
                    return key


        ClassDef_list = []
        for node in ast.walk(ast.parse(open(self.p_way).read())):
            if isinstance(node, ast.ClassDef):
                ClassDef_list.append(node.name)


        for i in range(len(main_list)):
            h = main_list[i]
            templist = []
            templist2 = {}
            key = 1
            count_cohesion=len(h)
            for k in range(0, len(h)-1):
                for g in range(k + 1, len(h)):
                    if (set(h[k]) & set(h[g])) != set():
                        count_cohesion-=1
                        # if any(i in val for val in templist2.values()):
                        #     yy = find_key(templist2, i)
                        #     templist2[yy].append(g)
                        # else:
                        #     templist2[key] = [i, g]
                        #     key = key + 1


            result+=ClassDef_list[i]+ '= '+ str(count_cohesion)+'\n'
        return result

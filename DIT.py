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

class DIT():
    def __init__(self,p,o):
        self.p_way=p
        self.co=o
    def count_DIT(self):
        result_object_ON=''
        result_object_OFF=''
        total_list={}
        total_list2={}
        for node in ast.walk(ast.parse(open(self.p_way).read())):
            if isinstance(node, ast.ClassDef):
                g = base_reader()
                g.visit(node)
                if g.base_name!=''and g.base_name!='object':
                    total_list2[node.name]=g.base_name
                if g.base_name!='':
                    total_list[node.name]=g.base_name


        # def get_keys(dic,value):
        #     return [k for k,v in dic.items() if v ==value]
        #
        # print(get_keys(total_list,'object'))
        #print('--- (object=ON)')
        for key,value in total_list.items():
            count=1
            as_key_value=value
            while as_key_value in total_list.keys():
                count+=1
                as_key_value=total_list[as_key_value]

            result_object_ON+= key+'= '+str(count)+'\n'

        #print('--- (object=OFF)')
        for key,value in total_list2.items():
            count=1
            as_key_value=value
            while as_key_value in total_list2.keys():
                count+=1
                as_key_value=total_list2[as_key_value]
            result_object_OFF+= key+'= '+str(count)+'\n'
        if self.co==1:
            return result_object_ON
        else:
            return result_object_OFF

# def get_keys(dic,value):
#     return [k for k,v in dic.items() if v ==value]
#
# print(get_keys(total_list,'NumberOfChildrenExample1'))
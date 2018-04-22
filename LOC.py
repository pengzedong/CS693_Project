path = 'SampleIncludingAll1.py'


class LOC():

    def __init__(self,p,c,e,i):
        self.p_way=p
        self.co=c
        self.em=e
        self.im=i
    def count_line(self):
        count = 0

        Commoncheck = False
        start_comment_index = 0

        index = 0
        global countPound
        global countBlank
        global imp
        global CommonLine
        countPound = 0
        imp=0
        countBlank = 0
        CommonLine = 0
        for file_line in open(self.p_way, 'r').readlines():

            index += 1
            if not Commoncheck:
                if file_line.startswith("'''") or file_line.startswith('"""') or file_line.startswith('""""'):
                    Commoncheck = True
                    start_comment_index = index
                elif file_line.__contains__("#"):
                    countPound += 1
                elif file_line == '' or file_line == '\n':
                    countBlank += 1
                elif file_line.startswith("import"):
                    imp += 1
                else:
                    count += 1
            else:
                if file_line.startswith("'''") or file_line.startswith('"""') or file_line.startswith('""""'):
                    Commoncheck = False

                    CommonLine += index - start_comment_index + 1
        if self.co==0:

            CommonLine=0
            countPound=0
        if self.em==0:

            countBlank=0
        if self.im==0:
            imp=0
        return 'LOC '+ ''+ str(count+CommonLine+countPound+countBlank+imp)
        # print("countPound =", countPound)
        # print("countBlank =", countBlank)
        # print("countCommon =", countCommon)
        # print("CommonLine =", CommonLine)
        # print('LOC (comments=ON,emptyLines=ON,imports=OFF)', CommonLine + countBlank + countPound + count)

# a=LOC(path)
#
# print(a.count_line())
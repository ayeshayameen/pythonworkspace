import  xlwt as write
class ExcelOperations:
     filePath ='F:\pythonworkspace\excelfile\\userInfo.xls'
     listOfLines = []

     def getDataFromFile(self):
          file=open('F:\pythonworkspace\excelfile\sampl.txt')
          for line in file.readlines():
               ExcelOperations.listOfLines.append(line.strip())



     def WritedataFromExcel(self):
          pass


if __name__ == '__main__':
    ob=ExcelOperations()
    ob.getDataFromFile()
    print(ExcelOperations.listOfLines)


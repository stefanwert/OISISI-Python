from parserr import Parser
import  os
import string

if __name__ == "__main__":
    p = Parser()
    p.parse('C:\\Users\\Petrovic\\Desktop\\stefan\\test-skup\\python-2.7.7-docs-html\\about.html')


    list_of_files={}

    for(dirpath,dirnames,filenames)in os.walk('C:\\Users\\Petrovic\\Desktop\\stefan\\test-skup'):
        for filename in filenames:
            if filename.endswith('.html'):
                #print(dirpath+filename)
                p.parse(dirpath+'\\'+filename)

    for str in p.links:
        print(str)



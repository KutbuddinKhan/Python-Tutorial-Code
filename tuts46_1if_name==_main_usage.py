# tuts46_1if_name==_main_usage
import sklearn

def printkkhan(string):
    return f"Ye string kkhan ko dedo {string}"

def add(num1, num2):
    return num1 + num2 + 5

print("and the name is", __name__)  #this is line is for general its not important
if __name__ == '__main__':

    print(printkkhan("Kasim"))

    add1 = add(5,5)
    print(add1)
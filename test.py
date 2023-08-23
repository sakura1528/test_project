def read_txt(path):
    with open(path) as file:
        lines = file.readlines()
        for line in lines:
            print(line)
            
read_txt("D:\\Users\\Desktop\\python (2)\\hosts-test")

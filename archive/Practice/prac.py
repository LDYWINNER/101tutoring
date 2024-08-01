from sys import argv

def celsius (f):
    return (f - 32) * 5 / 9

if __name__=="__main__":
    t = int(argv[1])
    print(celsius(t))



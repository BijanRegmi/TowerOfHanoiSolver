def Solver(n,L,M,R):
    if n:
        Solver(n-1,L,R,M)
        print("%s to %s"%(L,R))
        Solver(n-1,M,L,R)

def main():
    num = int(input("ENTER NUMBER OF DISKS "))
    while num<3:
        num = int(input("ENTER NUMBER GREATER THAN 2 "))
    source = "L"
    destination = "R"
    medium = "M"
    Solver(num,source,medium,destination)

if __name__ == "__main__":
    main()
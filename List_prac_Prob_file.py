#Program to write in file

def main():
    cities = ["Melbourne ", "Edmonton ","Halifax ","Dallas ","St.Johns "]
    outfile = open("cities.txt", "w")

    outfile.writelines(cities)

    outfile.close()

main()

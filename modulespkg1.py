# import modulespkg as m

# p = m.add3(2,3,4)
# print("Total = ",p)


from modulespkg import add3 as  a
# p = a(1,3,4)
# print("Total = ",p)

def main():
    p = a(1,3,4)
    print("Total = ",p)


if __name__ =='__main__':
    main()
def reverse(data):
    for index in range(len(data) -1, -1, -1):
        yield data[index]
        

def main():
##    rev = reverse("dragpsicle")
##    for char in rev:
##        print char

    data = "drapsicle"
    print list(data[i] for i in range(len(data) -1, -1, -1))

if __name__ == "__main__":
    main()

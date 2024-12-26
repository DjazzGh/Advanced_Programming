
while True:
        try:
         
            N = int(input("Enter a positive integer: "))

            if N <= 0:
                print("The number must be a positive.")
                continue

            for i in range(-N, 0):
                print(i)
            for i in range(1, N + 1):
                print(i)

            break

        except ValueError:
            print("Invalid type")



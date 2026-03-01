import math

class Vector:
    def addition(self, v1, v2):
        result = []
        for x, y in zip(v1, v2):
            result.append(float(x) + float(y))
        return result

    def matrix_trans(self, trans, to_trans_vector):
        result = []
        for matrix_row in trans:
            somme = 0
            for x, b in zip(matrix_row, to_trans_vector):
                somme = somme + (x * b)
            result.append(somme)
        return result

    def dot_prodcut(self, vector1, vector2):
        result = 0
        for v1, v2 in zip(vector1, vector2):
            result += v1 * v2
        return result

    def magnitude(self, vector):
        result = 0
        for v in vector:
            result += v**2
        return math.sqrt(result)

    def cosine_similarity(self, vector1, vector2):
        return self.dot_prodcut(vector1, vector2) / (self.magnitude(vector1) * self.magnitude(vector2))

def main():
    v = Vector()
    while True:
        print('----------- Linear algebra Operations -----------')
        print('1 - vector addition')
        print('2 - Linear Transformation')
        print('3 - Dot product')
        print('4 - Cosine similarity')
        print('5 - Exit')
        
        try:
            choice = int(input("enter your choice : "))
        except ValueError:
            print("enter a valid number")
            continue

        if choice == 1:
            try:
                dimension = int(input("enter dimension (2 or 3): "))
                if 1 < dimension <= 3:
                    v1_input = input('enter vector1 cordinates (separated by comma): ')
                    v2_input = input('enter vector2 cordinates (separated by comma): ')
                    
                    v1_list = v1_input.split(',')
                    v2_list = v2_input.split(',')
                    
                    if len(v1_list) == dimension and len(v2_list) == dimension:
                        v1 = [float(x) for x in v1_list]
                        v2 = [float(x) for x in v2_list]
                        res = v.addition(v1, v2)
                        print(f"result is : {res}")
                    else:
                        print(f"error: coordinates must match dimension {dimension}")
                else:
                    print("enter a valid dimension")
            except ValueError:
                print("error: invalid input format")
        
        elif choice == 2:
            try:
                rows = int(input("enter number of matrix rows: "))
                cols = int(input("enter number of matrix columns: "))
                matrix = []
                for i in range(rows):
                    row_input = input(f"enter row {i+1} coordinates (separated by comma): ")
                    row_list = row_input.split(',')
                    if len(row_list) != cols:
                        print(f"error: expected {cols} numbers")
                        break
                    matrix.append([float(x) for x in row_list])
                else:
                    vec_input = input(f"enter vector to transform ({cols} numbers separated by comma): ")
                    vec_list = vec_input.split(',')
                    if len(vec_list) == cols:
                        vector = [float(x) for x in vec_list]
                        res = v.matrix_trans(matrix, vector)
                        print(f"result is : {res}")
                    else:
                        print(f"error: vector must match columns {cols}")
            except ValueError:
                print("error: invalid input format")

        elif choice == 3:
            try:
                v1_input = input('enter vector1 cordinates (separated by comma): ')
                v2_input = input('enter vector2 cordinates (separated by comma): ')
                v1 = [float(x) for x in v1_input.split(',')]
                v2 = [float(x) for x in v2_input.split(',')]
                if len(v1) == len(v2):
                    res = v.dot_prodcut(v1, v2)
                    print(f"result is : {res}")
                else:
                    print("error: vectors must have same dimension")
            except ValueError:
                print("error: invalid input format")

        elif choice == 4:
            try:
                v1_input = input('enter vector1 cordinates (separated by comma): ')
                v1 = [float(x) for x in v1_input.split(',')]
                v2_input = input('enter vector2 cordinates (separated by comma): ')
                
                v2 = [float(x) for x in v2_input.split(',')]
                if len(v1) == len(v2):
                    res = v.cosine_similarity(v1, v2)
                    print(f"result is : {res}")
                    if res > 0.9:
                        print("Scale: Very Similar (Same direction)")
                    elif res > 0.5:
                        print("Scale: little bit Similar")
                    elif -0.1 <= res <= 0.1:
                        print("Scale: Not Similar")
                    elif res < -0.9:
                        print("Scale: Opposite directions")
                    else:
                        print("Scale: Different directions")
                else:
                    print("error: vectors must have same dimension")
            except ValueError:
                print("error: invalid input format")

        elif choice == 5:
            break

if __name__ == "__main__":
    main()

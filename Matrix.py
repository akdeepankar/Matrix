class Determinant:

    @staticmethod
    def order3(a11, a12, a13, a21, a22, a23, a31, a32, a33):
        temp_a1 = a22 * a33 - a23 * a32
        temp_b1 = a21 * a33 - a31 * a23
        temp_c1 = a21 * a32 - a31 * a22
        temp_a = a11 * temp_a1
        temp_b = a12 * temp_b1
        temp_c = a13 * temp_c1
        det = temp_a - temp_b + temp_c
        if det == 0:
            print("Determinant is 0")
        else:
            print(det)

        return det

def sqrt_newton(x: float, epsilon: float) -> float:
    def newton(x_div: float) -> float:
        return (x_div + x / x_div) / 2

    def is_fulfilled(x_div: float) -> bool:
        return abs(x_div ** 2 - x) < epsilon

    def sqrt_iter(x_div: float) -> float:
        return x_div if is_fulfilled(x_div) else sqrt_iter(newton(x_div))

    return sqrt_iter(x / 2)


if __name__ == '__main__':
    print(sqrt_newton(3, 0.1))

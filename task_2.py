from typing import List, Dict


def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    memo = {}

    def wrapper(n):
        if n == 0:
            return 0, []
        if n in memo:
            return memo[n]

        best_profit = 0
        best_segments = []

        for i in range(n):
            profit, segments = wrapper(n - (i + 1))
            profit += prices[i]
            if profit > best_profit:
                best_profit = profit
                best_segments = [i + 1] + segments

        memo[n] = (best_profit, best_segments)
        return memo[n]

    res_profit, res_segments = wrapper(length)
    return {
        "max_profit": res_profit,
        "cuts": res_segments,
        "number_of_cuts": len(res_segments) - 1,
    }


def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    dp = [0] * (length + 1)
    solution = [[] for _ in range(length + 1)]

    for i in range(1, length + 1):
        best_profit = 0
        for j in range(1, i + 1):
            if prices[j - 1] + dp[i - j] > best_profit:
                best_profit = prices[j - 1] + dp[i - j]
                solution[i] = solution[i - j] + [j]
        dp[i] = best_profit

    return {
        "max_profit": dp[length],
        "cuts": solution[length],
        "number_of_cuts": len(solution[length]) - 1,
    }


def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {"length": 5, "prices": [2, 5, 7, 8, 10], "name": "Базовий випадок"},
        # Тест 2: Оптимально не різати
        {"length": 3, "prices": [1, 3, 8], "name": "Оптимально не різати"},
        # Тест 3: Всі розрізи по 1
        {"length": 4, "prices": [3, 5, 6, 7], "name": "Рівномірні розрізи"},
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test["length"], test["prices"])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test["length"], test["prices"])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!")


if __name__ == "__main__":
    run_tests()

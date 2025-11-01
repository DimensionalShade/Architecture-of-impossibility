import random

def simulate(program):
    # Простейшая симуляция: случайно решаем, остановится ли программа
    return random.choice(["halts", "loops"])

def estimate_omega(programs):
    halted = 0
    for p in programs:
        if simulate(p) == "halts":
            halted += 1
    omega = halted / len(programs)
    print(f"Estimated Ω: {omega:.6f}")
    return omega

if __name__ == "__main__":
    # Пример: 1000 случайных программ
    dummy_programs = [f"P{i}" for i in range(1000)]
    estimate_omega(dummy_programs)

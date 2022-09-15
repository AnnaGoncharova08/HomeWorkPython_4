# 1 Вычислить число π c заданной точностью d

d = 20000

pi_num = 4 * (sum(1/x for x in range(1, d + 1, 4)) +
            sum(-1/x for x in range(3, d + 1, 4)))

print(pi_num)
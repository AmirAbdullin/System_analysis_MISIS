import numpy as np

class EntropyCalculator:
    def __init__(self, min_score, max_score):
        self.min_score = min_score
        self.max_score = max_score
        self.all_variants_count = max_score * max_score
        self.mults_count = self.all_variants_count
        self.sums_count = max_score * 2 - min_score * 2 + 1
        self.variants = np.zeros((self.sums_count, self.mults_count), dtype=int)

        self.calculate_variants()

    def calculate_variants(self):
        mult_norm = 1
        sum_norm = 2
        used_cols = set()

        for i in range(self.min_score, self.max_score + 1):
            for j in range(self.min_score, self.max_score + 1):
                cur_mult = i * j
                cur_sum = i + j

                used_cols.add(cur_mult - mult_norm)
                self.variants[cur_sum - sum_norm][cur_mult - mult_norm] += 1

        self.resized_variants = self.variants[:, list(used_cols)]

    def calculate_entropy(self):
        
        matrix_prob = self.resized_variants * 1.0 / self.all_variants_count

        PA = matrix_prob.sum(axis=1)
        PB = matrix_prob.sum(axis=0)


        def entropiya(p):
            return -p * np.log2(p) if p != 0 else 0

        vectorized_entropiya = np.vectorize(entropiya)

        matrix_entropy = vectorized_entropiya(matrix_prob)
        PA_entropy = vectorized_entropiya(PA)
        PB_entropy = vectorized_entropiya(PB)



        HA = np.sum(PA_entropy)
        HB = np.sum(PB_entropy)
        HAB = np.sum(matrix_entropy)
        HaB = HAB - HA
        HI = HB - HaB


        def to_fixed(num):
            return format(num, '.2f')

        return [to_fixed(HAB), to_fixed(HA), to_fixed(HB), to_fixed(HaB), to_fixed(HI)]

def task():
    min_score = 1
    max_score = 6

    calculator = EntropyCalculator(min_score, max_score)
    return calculator.calculate_entropy()

print(task())

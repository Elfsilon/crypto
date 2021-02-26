# from math import gcd, log
# from lab_1.gcd import gcd

# T pollard_p_1 (T n) {
# 	// параметры алгоритма, существенно влияют на производительность и качество поиска
# 	const T b = 13;
# 	const T q[] = { 2, 3, 5, 7, 11, 13 };
# 	// несколько попыток алгоритма
# 	T a = 5 % n;
# 	for (int j=0; j<10; j++){
# 		// ищем такое a, которое взаимно просто с n
# 		while (gcd (a, n) != 1){
# 			mulmod (a, a, n);
# 			a += 3;
# 			a %= n;
# 		}
# 		// вычисляем a^M
# 		for (size_t i = 0; i < sizeof q / sizeof q[0]; i++)
# 		{
# 			T qq = q[i];
# 			T e = (T) floor (log ((double)b) / log ((double)qq));
# 			T aa = powmod (a, powmod (qq, e, n), n);
# 			if (aa == 0)
# 				continue;
			
# 			// проверяем, не найден ли ответ
# 			T g = gcd (aa-1, n);
# 			if (1 < g && g < n)
# 				return g;
# 		}
# 	}
# 	// если ничего не нашли
# 	return 1;
# }

# def p_minus_one_factorization(n):
#     b = 13
#     q = [2, 3, 5, 7, 11, 13]

#     a = 5 % n
#     for j in range(0, 10):
#         while gcd(a, n) != 1:
#             a = a*a % n
#             a += 3
#             a %= n
        
#         # a^M
#         for i in range(0, q/q[0])
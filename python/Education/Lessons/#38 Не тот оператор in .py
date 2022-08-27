# Обратите внимание, что in в цикле — это не тот оператор in, про который рассказывалось в разделе «Продвинутые строки». for вместе с in — конструкция для создания цикла, то есть воспринимать ее надо как единое целое.

# Кстати «тот» оператор in может работать не только со строками, но и со списками
# x = [1, 2, 3, 4, "Hello"]
# print(1 in x)
# print("Bye" in x)
# print("Hello" in x)
# Если оператор in используется со списком, он проверяет наличие элемента в этом списке. Оцените простоту и дружественность Python — один и тот же оператор работает с разными данными похожим образом
# Помните, в разделе про словари была задача, в которой нужно было сделать простой каталог товаров? Итоговая программа работала, товары добавлялись в каталог и все было вроде бы неплохо.

# Но была и одна неприятная деталь: при каждом новом запуске этой программы каталог приходилось заполнять заново. Задача, конечно же, была учебной и в каталоге было совсем мало позиций.

# Представьте, однако, что таких товаров сотни и тысячи, как в настоящих магазинах или на настоящих складах. И каждый день в каталоге есть изменения: товары добавляются и удаляются. Так вот, для такой задачи, с тысячами или хотя бы с сотнями товаров, наша программа из задачи «Простой каталог товаров» совершенно непригодна.

# Разумеется, можно заставить программу работать вечно, например, с помощью бесконечного цикла, и тогда каталог не будет очищаться. Но это не решит проблему, если потребуется перезагрузка компьютера или, например, пропадет электричество.

# В общем, для того, чтобы сохранить каталог между запусками программы, нужно использовать файлы. Вся информация, которая записывается в файл, сохраняется на жестком диске компьютера. Кстати, программы, написанные вами, тоже хранятся в файлах.
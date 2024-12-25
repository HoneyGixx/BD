#encoding "utf-8"    // сообщаем парсеру о том, в какой кодировке написана грамматика
#GRAMMAR_ROOT S      // указываем корневой нетерминал грамматики
NF -> Noun<gnc-agr[1]> Adj<gnc-agr[1]>;
NF -> Adj<gnc-agr[1]> Noun<gnc-agr[1]>;
S -> NF;
//вывод в таблицу

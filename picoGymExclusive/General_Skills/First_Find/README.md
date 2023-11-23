# Lesson
- usage of `find` and `grep` command

# Memo
```console
$ find ./ -print
./
./13771.txt.utf-8
./14789.txt.utf-8
./acceptable_books
./acceptable_books/17879.txt.utf-8
./acceptable_books/17880.txt.utf-8
./acceptable_books/more_books
./acceptable_books/more_books/40723.txt.utf-8
./adequate_books
./adequate_books/44578.txt.utf-8
./adequate_books/46804-0.txt
./adequate_books/more_books
./adequate_books/more_books/.secret
./adequate_books/more_books/.secret/deeper_secrets
./adequate_books/more_books/.secret/deeper_secrets/deepest_secrets
./adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
./adequate_books/more_books/1023.txt.utf-8
./satisfactory_books
./satisfactory_books/16021.txt.utf-8
./satisfactory_books/23765.txt.utf-8
./satisfactory_books/more_books
./satisfactory_books/more_books/37121.txt.utf-8
$
$ grep -r "picoCTF" .
./adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt:picoCTF{f1nd_15_f457_ab443fd1}
$
```
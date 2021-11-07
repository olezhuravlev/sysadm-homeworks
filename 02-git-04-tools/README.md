# Домашнее задание к занятию «2.4. Инструменты Git»

Для выполнения заданий в этом разделе давайте склонируем репозиторий с исходным кодом 
терраформа https://github.com/hashicorp/terraform 

В виде результата напишите текстом ответы на вопросы и каким образом эти ответы были получены. 

---
**1. Найдите полный хеш и комментарий коммита, хеш которого начинается на `aefea`.**
 
**Первый способ:**<br/>
![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) $ git log --pretty=oneline | grep '^aefea'<br/>
aefead2207ef7e2aa5dc81a34aedf0cad4c32545 Update CHANGELOG.md

**Второй способ:**<br/>
![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) $ git show aefea<br/>
**Выведет:**<br/>
commit aefead2207ef7e2aa5dc81a34aedf0cad4c32545
Author: Alisdair McDiarmid <alisdair@users.noreply.github.com>
Date:   Thu Jun 18 10:29:58 2020 -0400

    Update CHANGELOG.md

...<br/>
(END)

**Третий способ - различные методы получения хэшей и комментариев:**<br/>
![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) $ git rev-parse aefea<br/>
aefead2207ef7e2aa5dc81a34aedf0cad4c32545

![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) $ git show-branch --independent aefea<br/>
aefead2207ef7e2aa5dc81a34aedf0cad4c32545

![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) $ git show-branch --sha1-name aefea<br/>
[aefead220] Update CHANGELOG.md

---
**2. Какому тегу соответствует коммит `85024d3`?**<br/>

**Первый способ:**<br/>
![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) $ git describe 85024d3<br/>
v0.12.23

**Второй способ:**<br/>
![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) $ git log 85024d3 -1<br/>
**Выведет:**<br/>
commit 85024d3100126de36331c6982bfaac02cdab9e76 (tag: v0.12.23)
Author: tf-release-bot <terraform@hashicorp.com>
Date:   Thu Mar 5 20:56:10 2020 +0000

    v0.12.23
...<br/>
(END)

**Третий способ:**<br/>
![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) $ git show 85024d3<br/>
**Выведет:**<br/>
commit 85024d3100126de36331c6982bfaac02cdab9e76 (tag: v0.12.23)
Author: tf-release-bot <terraform@hashicorp.com>
Date:   Thu Mar 5 20:56:10 2020 +0000

    v0.12.23
...<br/>
(END)


---
**3. Сколько родителей у коммита `b8d720`? Напишите их хеши.**<br/>

**Первый способ:**<br/>
![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) $ git log b8d720 -1<br/>
**Выведет:**<br/>
commit b8d720f8340221f2146e4e4870bf2ee0bc48f2d5<br/>
Merge: 56cd7859e 9ea88f22f<br/>
Author: Chris Griggs <cgriggs@hashicorp.com><br/>
Date:   Tue Jan 21 17:45:48 2020 -0800<br/>

    Merge pull request #23916 from hashicorp/cgriggs01-stable
    
    [Cherrypick] community links
(END)<br/>

Где в строке "Merge:" перечислены родители коммита.

Можно отформатировать вывод команды **git log** чтобы получить только хэши родительских коммитов:<br/>
![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) $ git log --pretty=%P b8d720 -1<br/>
**Выведет:**<br/>
56cd7859e05c36c06b56d013b55a252d0bb7e158 9ea88f22fc6269854151c571162c5bcf958bee2b<br/>
(END)

**Второй способ:**<br/>
![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) $ git show -s --pretty=%P b8d720 <br/>
**Выведет:**<br/>
56cd7859e05c36c06b56d013b55a252d0bb7e158 9ea88f22fc6269854151c571162c5bcf958bee2b<br/>
(END)

**Третий способ:**<br/>
![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) $ git rev-list --parents b8d720 -1<br/>
**Выведет:**<br/>
b8d720f8340221f2146e4e4870bf2ee0bc48f2d5 56cd7859e05c36c06b56d013b55a252d0bb7e158 9ea88f22fc6269854151c571162c5bcf958bee2b<br/>

где первый хеш - это хэш merge-коммита, а последующие - коммиты-родители.


---
**4. Перечислите хеши и комментарии всех коммитов которые были сделаны между тегами  v0.12.23 и v0.12.24.**<br/>

**Для получение диапазона сущностей между тегами используется метод git log с синтаксисом интервала:**<br/>
![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) $ git log v0.12.23...v0.12.24 --oneline<br/>
**Выведет:**<br/>
33ff1c03b (tag: v0.12.24) v0.12.24<br/>
b14b74c49 [Website] vmc provider links<br/>
3f235065b Update CHANGELOG.md<br/>
6ae64e247 registry: Fix panic when server is unreachable<br/>
5c619ca1b website: Remove links to the getting started guide's old location<br/>
06275647e Update CHANGELOG.md<br/>
d5f9411f5 command: Fix bug when using terraform login on Windows<br/>
4b6d06cc5 Update CHANGELOG.md<br/>
dd01a3507 Update CHANGELOG.md<br/>
225466bc3 Cleanup after v0.12.23 release<br/>

**_Если теги перечислены в порядке возрастания, то синтаксис с двумя точками (..) и тремя точками (...) будет работать одинаково,
т.к. Git покажет коммиты доступные из коммита второго тега, но недоступные из коммита первого тега, либо коммиты доступные только
из одного из тегов, что даёт одинаковый результат._**

**_Если же теги в команде перечислены в обратном порядке, то синтаксис с тремя точками (...) сработает по-прежнему, а синтаксис
с двумя точками (..) выведет пустой результат, потому что не существут коммитов доступных из первого тега, но  при этом недоступных из второго._** 

Также возможно использовать синтаксис **^** или **--not** означающий инвертирование условия:<br/>
![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) $ git log ^v0.12.23 v0.12.24 --oneline<br/>
![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) $ git log v0.12.24 --not v0.12.23 --oneline<br/>

---
**5. Найдите коммит в котором была создана функция `func providerSource`, ее определение в коде выглядит так `func providerSource(...)` (вместо троеточего перечислены аргументы).**<br/>

![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) $ git log -S "func providerSource" --source --all --reverse -p<br/>

где флаги:<br/>
**-S** позволяет искать измененную коммитом последовательность символов (строку);<br/>
**--source** покажет, какой веткой был внесены изменения;<br/>
**--all** определят, что поиск должен производится во всех ветках;<br/>
**--reverse** здесь для удобства, чтобы первый коммит, где искомая функция появилась был отображен вверху списка;<br/>
**-p** здесь также для удобства чтобы видеть текст изменений введенных коммитом и в этом тексте будет видна искомая функция (строка
будет предваряться знаком "+", что означает, что строка добавлена/изменен);<br/>

**Результат:**<br/>
commit 8c928e83589d90a031f811fae52a81be7153e82f refs/remotes/origin/alisdair/getproviders-retries-bad-branch-do-not-use<br/>
Author: Martin Atkins <mart@degeneration.co.uk><br/>
Date:   Thu Apr 2 18:04:39 2020 -0700<br/>
...<br/>
func providerSource(services *disco.Disco)** getproviders.Source {<br/>
...

---
**6. Найдите все коммиты в которых была изменена функция `globalPluginDirs`.**<br/>

Сначала найдем файл, в котором эта функция содержится:<br/>

![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+)  $ git log -S "func globalPluginDirs(" --source --all -p -n 1

**Результат:**<br/>
commit 8364383c359a6b738a436d1b7745ccdce178df47 refs/tags/v0.10.0-beta2
Author: Martin Atkins <mart@degeneration.co.uk>
Date:   Thu Apr 13 18:05:58 2017 -0700

    Push plugin discovery down into command package
    
    ...

**diff --git a/plugins.go b/plugins.go**

Из полученного результата следует, что функция `globalPluginDirs` расположена в файле **plugins.go**.

Далее найдем все коммиты с изменениями этой функции:<br/>

![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+)  $ git log -L :globalPluginDirs:plugins.go --pretty=short

**Результат:**<br/>
commit 78b12205587fe839f10d946ea3fdc06719decb05<br/>
Author: Pam Selle <204372+pselle@users.noreply.github.com><br/>

    Remove config.go and update things using its aliases
...<br/>
commit 52dbf94834cb970b510f2fba853a5b49ad9b1a46<br/>
Author: James Bardin <j.bardin@gmail.com><br/>

    keep .terraform.d/plugins for discovery
...<br/>
commit 41ab0aef7a0fe030e84018973a64135b11abcd70<br/>
Author: James Bardin <j.bardin@gmail.com><br/>

    Add missing OS_ARCH dir to global plugin paths
...<br/>
commit 66ebff90cdfaa6938f26f908c7ebad8d547fea17<br/>
Author: James Bardin <j.bardin@gmail.com><br/>

    move some more plugin search path logic to command
...<br/>
commit 8364383c359a6b738a436d1b7745ccdce178df47<br/>
Author: Martin Atkins <mart@degeneration.co.uk><br/>

    Push plugin discovery down into command packa
...<br/>
(END)

К сожалению, флаг **--pretty** здесь не работает и вывод измененных строк производится полностью.

---
**7. Кто автор функции `synchronizedWriters`?**<br/>

Как и в задании №5 используем поиск по строке:<br/>
![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) $ git log -S "func synchronizedWriters(" --source --all --reverse -p

**Как следует из вывода, функцию `synchronizedWriters` в первый раз объявил Martin Atkins 03 мая 2017 года, а через 3 года (30 ноября 2020 года) James Bardin её удалил как неиспользуемую:**


commit 5ac311e2a91e381e2f52234668b49ba670aa0fe5 refs/tags/v0.9.5<br/>
Author: Martin Atkins <mart@degeneration.co.uk><br/>
Date:   Wed May 3 16:25:41 2017 -0700<br/>

    main: synchronize writes to VT100-faker on Windows

...<br/>
+// synchronizedWriters takes a set of writers and returns wrappers that ensure<br/>
+// that only one write can be outstanding at a time across the whole set.<br/>
+func synchronizedWriters(targets ...io.Writer) []io.Writer {<br/>
...<br/>

commit bdfea50cc85161dea41be0fe3381fd98731ff786 refs/remotes/origin/rln-add-console-tutorial<br/>
Author: James Bardin <j.bardin@gmail.com><br/>
Date:   Mon Nov 30 18:02:04 2020 -0500<br/>

    remove unused
...<br/>
-// synchronizedWriters takes a set of writers and returns wrappers that ensure<br/>
-// that only one write can be outstanding at a time across the whole set.<br/>
-func synchronizedWriters(targets ...io.Writer) []io.Writer {<br/>
...<br/>

(END)

PowerShell 7.3.4
PS C:\Windows\System32> cd
PS C:\Users\truco> cd python
PS C:\Users\truco\python> git init
Initialized empty Git repository in C:/Users/truco/python/.git/
PS C:\Users\truco\python> git clone https://github.com/FML57/ArteProgramacion.git
Cloning into 'ArteProgramacion'...
info: please complete authentication in your browser...
warning: You appear to have cloned an empty repository.
PS C:\Users\truco\python> ac paint.py

cmdlet Add-Content at command pipeline position 1
Supply values for the following parameters:
Value[0]:
PS C:\Users\truco\python> ac snake.py

cmdlet Add-Content at command pipeline position 1
Supply values for the following parameters:
Value[0]:
PS C:\Users\truco\python> ac pacman.py

cmdlet Add-Content at command pipeline position 1
Supply values for the following parameters:
Value[0]:
PS C:\Users\truco\python> ac cannon.py

cmdlet Add-Content at command pipeline position 1
Supply values for the following parameters:
Value[0]:
PS C:\Users\truco\python> ac memory.py

cmdlet Add-Content at command pipeline position 1
Supply values for the following parameters:
Value[0]:
PS C:\Users\truco\python> git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ArteProgramacion/
        cannon.py
        memory.py
        pacman.py
        paint.py
        snake.py

nothing added to commit but untracked files present (use "git add" to track)
PS C:\Users\truco\python> git add *
error: 'ArteProgramacion/' does not have a commit checked out
fatal: adding files failed
PS C:\Users\truco\python> cd ArteProgramacion
PS C:\Users\truco\python\ArteProgramacion> git remote add Prueba https://github.com/FML57/ArteProgramacion.git
PS C:\Users\truco\python\ArteProgramacion> git add *
PS C:\Users\truco\python\ArteProgramacion> git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   cannon.py
        new file:   memory.py
        new file:   pacman.py
        new file:   paint.py
        new file:   snake.py

PS C:\Users\truco\python\ArteProgramacion> git commit -m "Generación de archivos py"
[main (root-commit) bd6490b] Generación de archivos py
 5 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 cannon.py
 create mode 100644 memory.py
 create mode 100644 pacman.py
 create mode 100644 paint.py
 create mode 100644 snake.py
PS C:\Users\truco\python\ArteProgramacion> git remote add Prueba https://github.com/FML57/ArteProgramacion.git
error: remote Prueba already exists.
PS C:\Users\truco\python\ArteProgramacion> git remote add cannon.py https://github.com/FML57/ArteProgramacion.git
PS C:\Users\truco\python\ArteProgramacion> git remote add origin https://github.com/FML57/ArteProgramacion.git
error: remote origin already exists.
PS C:\Users\truco\python\ArteProgramacion> git push -u origin main
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 262 bytes | 262.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/FML57/ArteProgramacion.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
PS C:\Users\truco\python\ArteProgramacion> git branch Paint
PS C:\Users\truco\python\ArteProgramacion> git checkout Paint
Switched to branch 'Paint'
PS C:\Users\truco\python\ArteProgramacion> git status
On branch Paint
nothing to commit, working tree clean
PS C:\Users\truco\python\ArteProgramacion> git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
PS C:\Users\truco\python\ArteProgramacion> git branch Snake
PS C:\Users\truco\python\ArteProgramacion> git branch Pacman
PS C:\Users\truco\python\ArteProgramacion> git branch Cannon
PS C:\Users\truco\python\ArteProgramacion> git branch Memory
PS C:\Users\truco\python\ArteProgramacion> git checkout Paint
Switched to branch 'Paint'
PS C:\Users\truco\python\ArteProgramacion> git status
On branch Paint
nothing to commit, working tree clean
PS C:\Users\truco\python\ArteProgramacion> git status
On branch Paint
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   paint.py

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\truco\python\ArteProgramacion> git add paint.py
PS C:\Users\truco\python\ArteProgramacion> git status
On branch Paint
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   paint.py

PS C:\Users\truco\python\ArteProgramacion> git restore --stages paint.py
error: unknown option `stages'
usage: git restore [<options>] [--source=<branch>] <file>...

    -s, --source <tree-ish>
                          which tree-ish to checkout from
    -S, --staged          restore the index
    -W, --worktree        restore the working tree (default)
    --ignore-unmerged     ignore unmerged entries
    --overlay             use overlay mode
    -q, --quiet           suppress progress reporting
    --recurse-submodules[=<checkout>]
                          control recursive updating of submodules
    --progress            force progress reporting
    -m, --merge           perform a 3-way merge with the new branch
    --conflict <style>    conflict style (merge, diff3, or zdiff3)
    -2, --ours            checkout our version for unmerged files
    -3, --theirs          checkout their version for unmerged files
    -p, --patch           select hunks interactively
    --ignore-skip-worktree-bits
                          do not limit pathspecs to sparse entries only
    --pathspec-from-file <file>
                          read pathspec from file
    --pathspec-file-nul   with --pathspec-from-file, pathspec elements are separated with NUL character

PS C:\Users\truco\python\ArteProgramacion> git restore --staged paint.py
PS C:\Users\truco\python\ArteProgramacion> git status
On branch Paint
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   paint.py

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\truco\python\ArteProgramacion> git checkout main
Switched to branch 'main'
M       paint.py
Your branch is up to date with 'origin/main'.
PS C:\Users\truco\python\ArteProgramacion> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   paint.py

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\truco\python\ArteProgramacion> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   cannon.py
        modified:   pacman.py
        modified:   paint.py
        modified:   snake.py

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\truco\python\ArteProgramacion> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   cannon.py
        modified:   memory.py
        modified:   pacman.py
        modified:   paint.py
        modified:   snake.py

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\truco\python\ArteProgramacion> git add *
PS C:\Users\truco\python\ArteProgramacion> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   cannon.py
        modified:   memory.py
        modified:   pacman.py
        modified:   paint.py
        modified:   snake.py

PS C:\Users\truco\python\ArteProgramacion> git commit -m "Códigos de referencia"
[main 389c1ad] Códigos de referencia
 5 files changed, 425 insertions(+)
PS C:\Users\truco\python\ArteProgramacion> git checkout Paint
Switched to branch 'Paint'
PS C:\Users\truco\python\ArteProgramacion> git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)
PS C:\Users\truco\python\ArteProgramacion> git push -u origin main
To https://github.com/FML57/ArteProgramacion.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/FML57/ArteProgramacion.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
PS C:\Users\truco\python\ArteProgramacion> git pull https://github.com/FML57/ArteProgramacion.git
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 6 (delta 3), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (6/6), 1.74 KiB | 49.00 KiB/s, done.
From https://github.com/FML57/ArteProgramacion
 * branch            HEAD       -> FETCH_HEAD
Merge made by the 'ort' strategy.
 README.md | 19 +++++++++++++++++++
 1 file changed, 19 insertions(+)
 create mode 100644 README.md
PS C:\Users\truco\python\ArteProgramacion> git status
On branch main
Your branch is ahead of 'origin/main' by 4 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
PS C:\Users\truco\python\ArteProgramacion> git push -u origin main
Enumerating objects: 21, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 16 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (9/9), 3.86 KiB | 989.00 KiB/s, done.
Total 9 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/FML57/ArteProgramacion.git
   af59901..111689c  main -> main
branch 'main' set up to track 'origin/main'.
PS C:\Users\truco\python\ArteProgramacion> git checkout Paint
Switched to branch 'Paint'
PS C:\Users\truco\python\ArteProgramacion> git pull main
fatal: 'main' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
PS C:\Users\truco\python\ArteProgramacion> git pull https://github.com/FML57/ArteProgramacion.git
From https://github.com/FML57/ArteProgramacion
 * branch            HEAD       -> FETCH_HEAD
Updating bd6490b..111689c
Fast-forward
 README.md |  19 ++++++++
 cannon.py |  70 +++++++++++++++++++++++++++
 memory.py |  73 +++++++++++++++++++++++++++++
 pacman.py | 159 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 paint.py  |  68 +++++++++++++++++++++++++++
 snake.py  |  55 ++++++++++++++++++++++
 6 files changed, 444 insertions(+)
 create mode 100644 README.md
PS C:\Users\truco\python\ArteProgramacion> git status
On branch Paint
nothing to commit, working tree clean
PS C:\Users\truco\python\ArteProgramacion> git checkout Snake
Switched to branch 'Snake'
PS C:\Users\truco\python\ArteProgramacion> git pull https://github.com/FML57/ArteProgramacion.git
From https://github.com/FML57/ArteProgramacion
 * branch            HEAD       -> FETCH_HEAD
Updating bd6490b..111689c
Fast-forward
 README.md |  19 ++++++++
 cannon.py |  70 +++++++++++++++++++++++++++
 memory.py |  73 +++++++++++++++++++++++++++++
 pacman.py | 159 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 paint.py  |  68 +++++++++++++++++++++++++++
 snake.py  |  55 ++++++++++++++++++++++
 6 files changed, 444 insertions(+)
 create mode 100644 README.md
PS C:\Users\truco\python\ArteProgramacion> git checkout Pacman
Switched to branch 'Pacman'
PS C:\Users\truco\python\ArteProgramacion> git pull https://github.com/FML57/ArteProgramacion.git
From https://github.com/FML57/ArteProgramacion
 * branch            HEAD       -> FETCH_HEAD
Updating bd6490b..111689c
Fast-forward
 README.md |  19 ++++++++
 cannon.py |  70 +++++++++++++++++++++++++++
 memory.py |  73 +++++++++++++++++++++++++++++
 pacman.py | 159 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 paint.py  |  68 +++++++++++++++++++++++++++
 snake.py  |  55 ++++++++++++++++++++++
 6 files changed, 444 insertions(+)
 create mode 100644 README.md
PS C:\Users\truco\python\ArteProgramacion> git checkout Cannon
Switched to branch 'Cannon'
PS C:\Users\truco\python\ArteProgramacion> git pull https://github.com/FML57/ArteProgramacion.git
From https://github.com/FML57/ArteProgramacion
 * branch            HEAD       -> FETCH_HEAD
Updating bd6490b..111689c
Fast-forward
 README.md |  19 ++++++++
 cannon.py |  70 +++++++++++++++++++++++++++
 memory.py |  73 +++++++++++++++++++++++++++++
 pacman.py | 159 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 paint.py  |  68 +++++++++++++++++++++++++++
 snake.py  |  55 ++++++++++++++++++++++
 6 files changed, 444 insertions(+)
 create mode 100644 README.md
PS C:\Users\truco\python\ArteProgramacion> git checkout Memory
Switched to branch 'Memory'
PS C:\Users\truco\python\ArteProgramacion> git pull https://github.com/FML57/ArteProgramacion.git
From https://github.com/FML57/ArteProgramacion
 * branch            HEAD       -> FETCH_HEAD
Updating bd6490b..111689c
Fast-forward
 README.md |  19 ++++++++
 cannon.py |  70 +++++++++++++++++++++++++++
 memory.py |  73 +++++++++++++++++++++++++++++
 pacman.py | 159 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 paint.py  |  68 +++++++++++++++++++++++++++
 snake.py  |  55 ++++++++++++++++++++++
 6 files changed, 444 insertions(+)
 create mode 100644 README.md
PS C:\Users\truco\python\ArteProgramacion> git checkout Paint
Switched to branch 'Paint'
PS C:\Users\truco\python\ArteProgramacion> git status
On branch Paint
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   paint.py

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\truco\python\ArteProgramacion> git add paint.py
PS C:\Users\truco\python\ArteProgramacion> git commit -m "Edición del código paint.py: triangulo, circulo y rectangulo"
[Paint 30cd6ee] Edición del código paint.py: triangulo, circulo y rectangulo
 1 file changed, 27 insertions(+), 4 deletions(-)
PS C:\Users\truco\python\ArteProgramacion> git checkout Snake
Switched to branch 'Snake'
PS C:\Users\truco\python\ArteProgramacion> git checkout Paint
Switched to branch 'Paint'
PS C:\Users\truco\python\ArteProgramacion> git status
On branch Paint
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   paint.py

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\truco\python\ArteProgramacion> git add paint.py
PS C:\Users\truco\python\ArteProgramacion> git status
On branch Paint
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   paint.py

PS C:\Users\truco\python\ArteProgramacion> git commit -m "Edición del código paint.py: Color nuevo"
[Paint 6df9ec6] Edición del código paint.py: Color nuevo
 1 file changed, 1 insertion(+)
PS C:\Users\truco\python\ArteProgramacion> git push main Paint
fatal: 'main' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
PS C:\Users\truco\python\ArteProgramacion> git push Paint
fatal: 'Paint' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
PS C:\Users\truco\python\ArteProgramacion> git push origin Paint
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 16 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 733 bytes | 366.00 KiB/s, done.
Total 6 (delta 4), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (4/4), completed with 2 local objects.
remote:
remote: Create a pull request for 'Paint' on GitHub by visiting:
remote:      https://github.com/FML57/ArteProgramacion/pull/new/Paint
remote:
To https://github.com/FML57/ArteProgramacion.git
 * [new branch]      Paint -> Paint
PS C:\Users\truco\python\ArteProgramacion> git push origin Snake
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'Snake' on GitHub by visiting:
remote:      https://github.com/FML57/ArteProgramacion/pull/new/Snake
remote:
To https://github.com/FML57/ArteProgramacion.git
 * [new branch]      Snake -> Snake
PS C:\Users\truco\python\ArteProgramacion> git push origin Pacman
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'Pacman' on GitHub by visiting:
remote:      https://github.com/FML57/ArteProgramacion/pull/new/Pacman
remote:
To https://github.com/FML57/ArteProgramacion.git
 * [new branch]      Pacman -> Pacman
PS C:\Users\truco\python\ArteProgramacion> git push origin Cannon
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'Cannon' on GitHub by visiting:
remote:      https://github.com/FML57/ArteProgramacion/pull/new/Cannon
remote:
To https://github.com/FML57/ArteProgramacion.git
 * [new branch]      Cannon -> Cannon
PS C:\Users\truco\python\ArteProgramacion> git push origin Memory
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'Memory' on GitHub by visiting:
remote:      https://github.com/FML57/ArteProgramacion/pull/new/Memory
remote:
To https://github.com/FML57/ArteProgramacion.git
 * [new branch]      Memory -> Memory
PS C:\Users\truco\python\ArteProgramacion> git checkout Snake
Switched to branch 'Snake'
PS C:\Users\truco\python\ArteProgramacion> git status
On branch Snake
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   snake.py

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\truco\python\ArteProgramacion> git add snake.py
PS C:\Users\truco\python\ArteProgramacion> git commit -m "Edición de snake.py: color aleatorio y spawn de comida aleatoria"
[Snake 8d24a98] Edición de snake.py: color aleatorio y spawn de comida aleatoria
 1 file changed, 9 insertions(+), 3 deletions(-)
PS C:\Users\truco\python\ArteProgramacion> git push origin Snake
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 559 bytes | 559.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/FML57/ArteProgramacion.git
   111689c..8d24a98  Snake -> Snake
PS C:\Users\truco\python\ArteProgramacion> git checkout Pacman
Switched to branch 'Pacman'
PS C:\Users\truco\python\ArteProgramacion> git status
On branch Pacman
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   pacman.py

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\truco\python\ArteProgramacion> git add pacman.py
PS C:\Users\truco\python\ArteProgramacion> git commit -m "Edición de pacman.py: mapa diferente, fantasmas más rápidos"
[Pacman d4a252d] Edición de pacman.py: mapa diferente, fantasmas más rápidos
 1 file changed, 18 insertions(+), 8 deletions(-)
PS C:\Users\truco\python\ArteProgramacion> git status
On branch Pacman
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   pacman.py

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\truco\python\ArteProgramacion> git add pacman.py
PS C:\Users\truco\python\ArteProgramacion> git commit -m "Edición de pacman.py: Movimientos separados de fantasmas y pacman, fantasmas más inteligentes"
[Pacman cb66572] Edición de pacman.py: Movimientos separados de fantasmas y pacman, fantasmas más inteligentes
 1 file changed, 50 insertions(+), 39 deletions(-)
PS C:\Users\truco\python\ArteProgramacion> git push origin Pacman
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 16 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 1.90 KiB | 648.00 KiB/s, done.
Total 6 (delta 4), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (4/4), completed with 2 local objects.
To https://github.com/FML57/ArteProgramacion.git
   111689c..cb66572  Pacman -> Pacman
PS C:\Users\truco\python\ArteProgramacion> git checkout Cannon
Switched to branch 'Cannon'
PS C:\Users\truco\python\ArteProgramacion> git status
On branch Cannon
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   cannon.py

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\truco\python\ArteProgramacion> git add cannon.py
PS C:\Users\truco\python\ArteProgramacion> git commit -m "Edición de cannon.py: objetivos y bala más rápidos, objetivos se reposicionan"
[Cannon 31a4317] Edición de cannon.py: objetivos y bala más rápidos, objetivos se reposicionan
 1 file changed, 9 insertions(+), 2 deletions(-)
PS C:\Users\truco\python\ArteProgramacion> git push origin Cannon
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 486 bytes | 486.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/FML57/ArteProgramacion.git
   111689c..31a4317  Cannon -> Cannon
PS C:\Users\truco\python\ArteProgramacion> git checkout Memory
Switched to branch 'Memory'
PS C:\Users\truco\python\ArteProgramacion> git add memory.py
PS C:\Users\truco\python\ArteProgramacion> git commit -m "Edición de memory.py: Cambio a letras y cuenta de toques"
[Memory a52fdb6] Edición de memory.py: Cambio a letras y cuenta de toques
 1 file changed, 8 insertions(+), 3 deletions(-)
PS C:\Users\truco\python\ArteProgramacion> git add memory.py
PS C:\Users\truco\python\ArteProgramacion> git commit -m "Edición de memory.py: Detección al revelar letras y centrado de texto"
[Memory 37ef84d] Edición de memory.py: Detección al revelar letras y centrado de texto
 1 file changed, 11 insertions(+), 4 deletions(-)
PS C:\Users\truco\python\ArteProgramacion> git push origin Memory
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 16 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 1.01 KiB | 518.00 KiB/s, done.
Total 6 (delta 4), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (4/4), completed with 2 local objects.
To https://github.com/FML57/ArteProgramacion.git
   111689c..37ef84d  Memory -> Memory
PS C:\Users\truco\python\ArteProgramacion> git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
PS C:\Users\truco\python\ArteProgramacion> git merge Paint
Updating 111689c..6df9ec6
Fast-forward
 paint.py | 32 ++++++++++++++++++++++++++++----
 1 file changed, 28 insertions(+), 4 deletions(-)
PS C:\Users\truco\python\ArteProgramacion> git merge Snake
Merge made by the 'ort' strategy.
 snake.py | 12 +++++++++---
 1 file changed, 9 insertions(+), 3 deletions(-)
PS C:\Users\truco\python\ArteProgramacion> git merge Pacman
Merge made by the 'ort' strategy.
 pacman.py | 107 +++++++++++++++++++++++++++++++++++++-------------------------
 1 file changed, 64 insertions(+), 43 deletions(-)
PS C:\Users\truco\python\ArteProgramacion> git merge Cannon
Merge made by the 'ort' strategy.
 cannon.py | 11 +++++++++--
 1 file changed, 9 insertions(+), 2 deletions(-)
PS C:\Users\truco\python\ArteProgramacion> git merge Memory
Merge made by the 'ort' strategy.
 memory.py | 26 +++++++++++++++++++-------
 1 file changed, 19 insertions(+), 7 deletions(-)
PS C:\Users\truco\python\ArteProgramacion> git status
On branch main
Your branch is ahead of 'origin/main' by 12 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
PS C:\Users\truco\python\ArteProgramacion> git push -u origin main
Enumerating objects: 13, done.
Counting objects: 100% (13/13), done.
Delta compression using up to 16 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (8/8), 1.11 KiB | 568.00 KiB/s, done.
Total 8 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 1 local object.
To https://github.com/FML57/ArteProgramacion.git
   111689c..eb6417a  main -> main
branch 'main' set up to track 'origin/main'.
PS C:\Users\truco\python\ArteProgramacion> git merge Paint
Already up to date.
PS C:\Users\truco\python\ArteProgramacion>

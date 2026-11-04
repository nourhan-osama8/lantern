E1

```
$ git remote -v
origin  https://github.com/nourhan-osama8/lantern.git (fetch)
origin  https://github.com/nourhan-osama8/lantern.git (push)

```

E2

```
$ git status
On branch main
Your branch is ahead of 'origin/main' by 3 commits.
  (use "git push" to publish your local commits)
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   notes.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   notes.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        __pycache__/
        evidence/


$ git diff --cached
diff --git a/notes.txt b/notes.txt
index 4c9eee4..9f9ae6d 100644
--- a/notes.txt
+++ b/notes.txt
@@ -1 +1,2 @@
 This is a temporary draft file.
+This line is staged.

$ git diff
diff --git a/notes.txt b/notes.txt
index 9f9ae6d..e0baa76 100644
--- a/notes.txt
+++ b/notes.txt
@@ -1,2 +1,3 @@
 This is a temporary draft file.
 This line is staged.
+This line is not staged.
warning: LF will be replaced by CRLF in notes.txt.
The file will have its original line endings in your working directory.

```

E4

```
$ git log --oneline --graph --decorate --all
*   18a6e8b (HEAD -> main) merge: combine title cleanup and completion status
|\
| * 93fa96d (feature/done-flag) feat: add completion status to new tasks
* | 113d7d8 (fix/strip-title) fix: strip whitespace from task titles
|/
*   9fc6781 (origin/main, origin/HEAD) Merge remote-tracking branch 'origin/main' into main
|\
| * 5d6a705 docs(storage): add comment
| * 1c47c09 chore(scratch): remove temporary placeholder
| * 376d95d chore(scratch): add temporary placeholder
| * ff03d6b docs(usage): document basic commands
| * 52d21e3 feat(storage): add task persistence
* | 8d0e60b chore: rename draft file to notes
* | 3952342 chore: add draft placeholder file
* | 4cf88d5 feat: add initial task and CLI modules
|/
*   cd23004 Merge branch 'main' of github.com:nourhan-osama8/lantern
|\
| * dcf0989 docs: add team information to README
* | 3434987 docs(README): add team member
|/
* cdb6915 Initial commit

```

E5
drill (a)

```
$ git reflog --oneline
...
0b809ef HEAD@{2}: pull origin main: Merge made by the 'recursive' strategy.
22ae95d HEAD@{3}: commit (amend): docs: practice commit amendment drill
59d4ae7 HEAD@{4}: commit: docs: practce commit amendmant drill
26e380a HEAD@{5}: commit: chore: ignore local environment files
...

```

E5
drill (c)

```
$ git reflog --oneline
0b809ef HEAD@{0}: reset: moving to 0b809ef
37f19d7 HEAD@{1}: commit: docs: add reflog recovery drill note
0b809ef HEAD@{2}: pull origin main: Merge made by the 'recursive' strategy.
...

$ git reset --hard 37f19d7
HEAD is now at 37f19d7 docs: add reflog recovery drill note

$ git log -2 --oneline
37f19d7 docs: add reflog recovery drill note
0b809ef Merge branch 'main' of https://github.com/nourhan-osama8/lantern into main

```

E7

```
$ git commit -m "test: verify main branch protection"
[main 08b961e] test: verify main branch protection
 1 file changed, 1 insertion(+)

$ git push origin main
Fatal: HttpRequestException encountered.
Username for 'https://github.com': nourhan-osama8
Counting objects: 3, done.
Delta compression using up to 16 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 338 bytes | 0 bytes/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote: error: GH013: Repository rule violations found for refs/heads/main.
remote: Review all repository rules at https://github.com/nourhan-osama8/lantern/rules?ref=refs%2Fheads%2Fmain
remote:
remote: - Changes must be made through a pull request.
remote:
To https://github.com/nourhan-osama8/lantern.git
 ! [remote rejected] main -> main (push declined due to repository rule violations)
error: failed to push some refs to 'https://github.com/nourhan-osama8/lantern.git'

```
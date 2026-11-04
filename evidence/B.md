# E1
```text
$ git remote -v
origin  git@github.com:nourhan-osama8/lantern.git (fetch)
origin  git@github.com:nourhan-osama8/lantern.git (push)
```

# E3
```text
$ git log --oneline -2
5d6a705 (HEAD -> main) docs(storage): add comment
1c47c09 chore(scratch): remove temporary placeholder

$ git rev-parse 5d6a705^{tree}
640cab388360de78a2e5accc0d7f30c9233f50c8

$ git rev-parse 1c47c09^{tree}
612a49f21b19c528e9571b1293c26d478f8786d3

$ git rev-parse 5d6a705:README.md
41b579804556819cbd054f2dd8853c8bb2ef6764

$ git rev-parse 1c47c09:README.md
41b579804556819cbd054f2dd8853c8bb2ef6764

$ git rev-parse 5d6a705:storage.py
ba77c475627f8cbec23afbc4eb7d3cbaa0cffdff

$ git rev-parse 1c47c09:storage.py
06bd0aeb046aba93192b6959f6218495934ebe92
```

# E4
```text
$ git log --graph --oneline --all
*   7d97989 (HEAD -> main) Merge branch 'feature/pretty-json'
|\
| * 69ee914 feat(storage): write json with indent of 2
* | 6cbf433 fix(storage): write keys in sorted order
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

# E5
drill (b)
```text
$ git reflog
9f1f51c (HEAD -> main, origin/main, origin/HEAD, docs/usage-heading) HEAD@{0}: merge docs/usage-heading: Fast-forward
3b2aed5 HEAD@{1}: reset: moving to origin/main
9f1f51c (HEAD -> main, origin/main, origin/HEAD, docs/usage-heading) HEAD@{2}: commit: docs: add heading to usage
3b2aed5 HEAD@{3}: commit: fix: untrack junk files and add gitignore
8c4a658 HEAD@{4}: pull origin main: Merge made by the 'ort' strategy.
20cff7e HEAD@{5}: commit: chore: add logging and run module
7d97989 HEAD@{6}: commit (merge): Merge branch 'feature/pretty-json'
6cbf433 HEAD@{7}: merge fix/stable-key-order: Fast-forward
9fc6781 HEAD@{8}: checkout: moving from feature/pretty-json to main
69ee914 HEAD@{9}: commit: feat(storage): write json with indent of 2
9fc6781 HEAD@{10}: checkout: moving from main to feature/pretty-json
9fc6781 HEAD@{11}: checkout: moving from fix/stable-key-order to main
6cbf433 HEAD@{12}: commit: fix(storage): write keys in sorted order
9fc6781 HEAD@{13}: checkout: moving from main to fix/stable-key-order
9fc6781 HEAD@{14}: pull origin main: Fast-forward
5d6a705 HEAD@{15}: commit: docs(storage): add comment
1c47c09 HEAD@{16}: commit: chore(scratch): remove temporary placeholder
376d95d HEAD@{17}: commit: chore(scratch): add temporary placeholder
ff03d6b HEAD@{18}: commit: docs(usage): document basic commands
52d21e3 HEAD@{19}: commit: feat(storage): add task persistence
cd23004 HEAD@{20}: commit (merge): Merge branch 'main' of github.com:nourhan-osama8/lantern
3434987 HEAD@{21}: commit: docs(README): add team member
cdb6915 HEAD@{22}: clone: from github.com:nourhan-osama8/lantern.git

```

# E6
```text
$ git stash list
stash@{0}: On feature/list-sort: WIP: list sort feature

```

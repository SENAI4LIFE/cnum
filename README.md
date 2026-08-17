# cnum

Cálculo Numérico

## Git

### Configuração

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
git config --list
```

### Repositório

```bash
git init
git clone URL_DO_REPOSITORIO
```

### Status e alterações

```bash
git status
git diff
git diff --staged
```

### Adicionar e salvar alterações

```bash
git add .
git add arquivo
git commit -m "mensagem"
```

### Histórico

```bash
git log
git log --oneline
git log --oneline --graph --decorate --all
```

### Branches

```bash
git branch
git branch -a

git branch nome-da-branch
git switch nome-da-branch
git switch -c nome-da-branch

git branch -d nome-da-branch
git branch -D nome-da-branch
```

### Remotos

```bash
git remote -v
git remote add origin URL_DO_REPOSITORIO
git remote set-url origin URL_DO_REPOSITORIO
git remote remove origin
```

### GitHub

```bash
git push
git push -u origin main

git pull
git pull origin main

git fetch
```

### Merge

```bash
git merge nome-da-branch
git merge --abort
```

### Rebase

```bash
git rebase main
git rebase --continue
git rebase --abort
```

### Desfazer alterações

```bash
git restore arquivo
git restore --staged arquivo

git reset --soft HEAD~1
git reset HEAD~1
git reset --hard HEAD~1
```

### Stash

```bash
git stash
git stash list
git stash apply
git stash pop
git stash drop stash@{0}
git stash clear
```

### Tags

```bash
git tag
git tag v1.0.0
git tag -a v1.0.0 -m "Versão 1.0.0"

git push origin v1.0.0
git push origin --tags

git tag -d v1.0.0
git push origin --delete v1.0.0
```

### Arquivos

```bash
git rm arquivo
git rm --cached arquivo
```

## GitHub CLI

### Autenticação

```bash
gh auth login
gh auth status
```

### Repositórios

```bash
gh repo create
gh repo clone usuario/cnum
gh repo view
gh repo view --web
```

### Issues

```bash
gh issue list
gh issue create
gh issue view NUMERO
gh issue close NUMERO
gh issue reopen NUMERO
```

### Pull Requests

```bash
gh pr list
gh pr create
gh pr view NUMERO
gh pr checkout NUMERO
gh pr merge NUMERO
gh pr close NUMERO
```

### Actions

```bash
gh workflow list
gh workflow run NOME_DO_WORKFLOW

gh run list
gh run view ID
gh run view ID --log
gh run cancel ID
```

## Fluxo básico

```bash
git clone URL_DO_REPOSITORIO
cd cnum

git switch -c nome-da-branch

git status
git add .
git commit -m "mensagem"

git push -u origin nome-da-branch
```

Para atualizar a branch principal:

```bash
git switch main
git pull origin main
```

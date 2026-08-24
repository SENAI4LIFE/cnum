# cnum

Cálculo Numérico

## Git

### Configuração

Define o nome do usuário nos commits.

```bash
git config --global user.name "Seu Nome"
```

Define o e-mail associado aos commits.

```bash
git config --global user.email "seu@email.com"
```

Exibe as configurações atuais do Git.

```bash
git config --list
```

## Repositório

Inicializa um novo repositório Git no diretório atual.

```bash
git init
```

Copia um repositório existente para o computador.

```bash
git clone URL_DO_REPOSITORIO
```

## Status e alterações

Mostra o estado atual do repositório e os arquivos modificados.

```bash
git status
```

Mostra as alterações ainda não adicionadas ao staging.

```bash
git diff
```

Mostra as alterações adicionadas ao staging.

```bash
git diff --staged
```

## Adicionar e salvar alterações

Adiciona um arquivo ao staging.

```bash
git add arquivo
```

Adiciona as alterações do diretório atual ao staging.

```bash
git add .
```

Registra as alterações adicionadas ao staging em um novo commit.

```bash
git commit -m "mensagem"
```

## Histórico

Exibe o histórico de commits.

```bash
git log
```

Exibe o histórico de forma resumida.

```bash
git log --oneline
```

Exibe o histórico resumido com o relacionamento entre branches.

```bash
git log --oneline --graph --decorate --all
```

## Branches

Lista as branches locais.

```bash
git branch
```

Lista as branches locais e remotas.

```bash
git branch -a
```

Cria uma nova branch sem mudar para ela.

```bash
git branch nome-da-branch
```

Muda para uma branch existente.

```bash
git switch nome-da-branch
```

Cria uma nova branch e muda para ela.

```bash
git switch -c nome-da-branch
```

Exclui uma branch local que já foi mesclada.

```bash
git branch -d nome-da-branch
```

Força a exclusão de uma branch local.

```bash
git branch -D nome-da-branch
```

## Repositórios remotos

Exibe os repositórios remotos configurados.

```bash
git remote -v
```

Adiciona um repositório remoto com o nome `origin`.

```bash
git remote add origin URL_DO_REPOSITORIO
```

Altera o endereço de um repositório remoto.

```bash
git remote set-url origin URL_DO_REPOSITORIO
```

Remove um repositório remoto da configuração local.

```bash
git remote remove origin
```

## GitHub

Envia os commits locais para o repositório remoto.

```bash
git push
```

Envia a branch `main` para o GitHub e define `origin/main` como referência padrão.

```bash
git push -u origin main
```

Baixa e integra as alterações do repositório remoto.

```bash
git pull
```

Baixa e integra as alterações da branch `main` do remoto `origin`.

```bash
git pull origin main
```

Baixa informações do repositório remoto sem alterar a branch atual.

```bash
git fetch
```

## Merge

Integra uma branch à branch atual.

```bash
git merge nome-da-branch
```

Cancela um merge em andamento.

```bash
git merge --abort
```

## Rebase

Reaplica os commits da branch atual sobre a `main`.

```bash
git rebase main
```

Continua um rebase após a resolução de conflitos.

```bash
git rebase --continue
```

Cancela um rebase em andamento.

```bash
git rebase --abort
```

## Desfazer alterações

Descarta as alterações não commitadas de um arquivo.

```bash
git restore arquivo
```

Remove um arquivo do staging sem apagar suas alterações.

```bash
git restore --staged arquivo
```

Remove o último commit, mantendo as alterações no staging.

```bash
git reset --soft HEAD~1
```

Remove o último commit, mantendo as alterações nos arquivos.

```bash
git reset HEAD~1
```

Remove o último commit e descarta as alterações associadas.

```bash
git reset --hard HEAD~1
```

## Stash

Guarda temporariamente as alterações não commitadas.

```bash
git stash
```

Lista as alterações armazenadas no stash.

```bash
git stash list
```

Aplica o último stash sem removê-lo da lista.

```bash
git stash apply
```

Aplica o último stash e o remove da lista.

```bash
git stash pop
```

Remove um stash específico.

```bash
git stash drop stash@{0}
```

Remove todos os stashes.

```bash
git stash clear
```

## Tags

Lista as tags existentes.

```bash
git tag
```

Cria uma tag simples para marcar uma versão.

```bash
git tag v1.0.0
```

Cria uma tag anotada com uma mensagem.

```bash
git tag -a v1.0.0 -m "Versão 1.0.0"
```

Envia uma tag específica para o repositório remoto.

```bash
git push origin v1.0.0
```

Envia todas as tags locais para o repositório remoto.

```bash
git push origin --tags
```

Exclui uma tag local.

```bash
git tag -d v1.0.0
```

Exclui uma tag do repositório remoto.

```bash
git push origin --delete v1.0.0
```

## Arquivos

Remove um arquivo do computador e registra a remoção no Git.

```bash
git rm arquivo
```

Remove um arquivo do controle do Git, mantendo-o no computador.

```bash
git rm --cached arquivo
```

## GitHub CLI

### Autenticação

Realiza o login do GitHub CLI na conta do GitHub.

```bash
gh auth login
```

Exibe o estado da autenticação atual.

```bash
gh auth status
```

### Repositórios

Cria um novo repositório no GitHub.

```bash
gh repo create
```

Clona um repositório do GitHub.

```bash
gh repo clone usuario/cnum
```

Exibe informações sobre o repositório atual.

```bash
gh repo view
```

Abre o repositório atual no navegador.

```bash
gh repo view --web
```

### Issues

Lista as Issues do repositório.

```bash
gh issue list
```

Cria uma nova Issue.

```bash
gh issue create
```

Exibe uma Issue específica.

```bash
gh issue view NUMERO
```

Fecha uma Issue.

```bash
gh issue close NUMERO
```

Reabre uma Issue fechada.

```bash
gh issue reopen NUMERO
```

### Pull Requests

Lista os Pull Requests do repositório.

```bash
gh pr list
```

Cria um novo Pull Request.

```bash
gh pr create
```

Exibe um Pull Request específico.

```bash
gh pr view NUMERO
```

Baixa e muda para a branch de um Pull Request.

```bash
gh pr checkout NUMERO
```

Faz o merge de um Pull Request.

```bash
gh pr merge NUMERO
```

Fecha um Pull Request.

```bash
gh pr close NUMERO
```

### GitHub Actions

Lista os workflows configurados no repositório.

```bash
gh workflow list
```

Executa manualmente um workflow.

```bash
gh workflow run NOME_DO_WORKFLOW
```

Lista as execuções recentes dos workflows.

```bash
gh run list
```

Exibe informações sobre uma execução específica.

```bash
gh run view ID
```

Exibe os logs de uma execução.

```bash
gh run view ID --log
```

Cancela uma execução em andamento.

```bash
gh run cancel ID
```

## Fluxo básico

Baixa o projeto do GitHub.

```bash
git clone URL_DO_REPOSITORIO
```

Entra no diretório do projeto.

```bash
cd cnum
```

Cria uma branch para trabalhar em uma alteração.

```bash
git switch -c nome-da-branch
```

Verifica as alterações realizadas.

```bash
git status
```

Adiciona as alterações ao staging.

```bash
git add .
```

Registra as alterações em um commit.

```bash
git commit -m "mensagem"
```

Envia a branch para o GitHub.

```bash
git push -u origin nome-da-branch
```

Para atualizar a branch principal:

Muda para a branch `main`.

```bash
git switch main
```

Atualiza a `main` com as alterações do GitHub.

```bash
git pull origin main
```

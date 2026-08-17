# cnum

Cálculo Numérico

## Git

### Configuração

```bash
git config --global user.name "Seu Nome"
```

Define o nome do usuário nos commits.

```bash
git config --global user.email "seu@email.com"
```

Define o e-mail associado aos commits.

```bash
git config --list
```

Exibe as configurações atuais do Git.

## Repositório

```bash
git init
```

Inicializa um novo repositório Git no diretório atual.

```bash
git clone URL_DO_REPOSITORIO
```

Copia um repositório existente para o computador.

## Status e alterações

```bash
git status
```

Mostra o estado atual do repositório e os arquivos modificados.

```bash
git diff
```

Mostra as alterações ainda não adicionadas ao staging.

```bash
git diff --staged
```

Mostra as alterações adicionadas ao staging.

## Adicionar e salvar alterações

```bash
git add arquivo
```

Adiciona um arquivo ao staging.

```bash
git add .
```

Adiciona as alterações do diretório atual ao staging.

```bash
git commit -m "mensagem"
```

Registra as alterações adicionadas ao staging em um novo commit.

## Histórico

```bash
git log
```

Exibe o histórico de commits.

```bash
git log --oneline
```

Exibe o histórico de forma resumida.

```bash
git log --oneline --graph --decorate --all
```

Exibe o histórico resumido com o relacionamento entre branches.

## Branches

```bash
git branch
```

Lista as branches locais.

```bash
git branch -a
```

Lista as branches locais e remotas.

```bash
git branch nome-da-branch
```

Cria uma nova branch sem mudar para ela.

```bash
git switch nome-da-branch
```

Muda para uma branch existente.

```bash
git switch -c nome-da-branch
```

Cria uma nova branch e muda para ela.

```bash
git branch -d nome-da-branch
```

Exclui uma branch local que já foi mesclada.

```bash
git branch -D nome-da-branch
```

Força a exclusão de uma branch local.

## Repositórios remotos

```bash
git remote -v
```

Exibe os repositórios remotos configurados.

```bash
git remote add origin URL_DO_REPOSITORIO
```

Adiciona um repositório remoto com o nome `origin`.

```bash
git remote set-url origin URL_DO_REPOSITORIO
```

Altera o endereço de um repositório remoto.

```bash
git remote remove origin
```

Remove um repositório remoto da configuração local.

## GitHub

```bash
git push
```

Envia os commits locais para o repositório remoto.

```bash
git push -u origin main
```

Envia a branch `main` para o GitHub e define `origin/main` como referência padrão.

```bash
git pull
```

Baixa e integra as alterações do repositório remoto.

```bash
git pull origin main
```

Baixa e integra as alterações da branch `main` do remoto `origin`.

```bash
git fetch
```

Baixa informações do repositório remoto sem alterar a branch atual.

## Merge

```bash
git merge nome-da-branch
```

Integra uma branch à branch atual.

```bash
git merge --abort
```

Cancela um merge em andamento.

## Rebase

```bash
git rebase main
```

Reaplica os commits da branch atual sobre a `main`.

```bash
git rebase --continue
```

Continua um rebase após a resolução de conflitos.

```bash
git rebase --abort
```

Cancela um rebase em andamento.

## Desfazer alterações

```bash
git restore arquivo
```

Descarta as alterações não commitadas de um arquivo.

```bash
git restore --staged arquivo
```

Remove um arquivo do staging sem apagar suas alterações.

```bash
git reset --soft HEAD~1
```

Remove o último commit, mantendo as alterações no staging.

```bash
git reset HEAD~1
```

Remove o último commit, mantendo as alterações nos arquivos.

```bash
git reset --hard HEAD~1
```

Remove o último commit e descarta as alterações associadas.

## Stash

```bash
git stash
```

Guarda temporariamente as alterações não commitadas.

```bash
git stash list
```

Lista as alterações armazenadas no stash.

```bash
git stash apply
```

Aplica o último stash sem removê-lo da lista.

```bash
git stash pop
```

Aplica o último stash e o remove da lista.

```bash
git stash drop stash@{0}
```

Remove um stash específico.

```bash
git stash clear
```

Remove todos os stashes.

## Tags

```bash
git tag
```

Lista as tags existentes.

```bash
git tag v1.0.0
```

Cria uma tag simples para marcar uma versão.

```bash
git tag -a v1.0.0 -m "Versão 1.0.0"
```

Cria uma tag anotada com uma mensagem.

```bash
git push origin v1.0.0
```

Envia uma tag específica para o repositório remoto.

```bash
git push origin --tags
```

Envia todas as tags locais para o repositório remoto.

```bash
git tag -d v1.0.0
```

Exclui uma tag local.

```bash
git push origin --delete v1.0.0
```

Exclui uma tag do repositório remoto.

## Arquivos

```bash
git rm arquivo
```

Remove um arquivo do computador e registra a remoção no Git.

```bash
git rm --cached arquivo
```

Remove um arquivo do controle do Git, mantendo-o no computador.

## GitHub CLI

### Autenticação

```bash
gh auth login
```

Realiza o login do GitHub CLI na conta do GitHub.

```bash
gh auth status
```

Exibe o estado da autenticação atual.

### Repositórios

```bash
gh repo create
```

Cria um novo repositório no GitHub.

```bash
gh repo clone usuario/cnum
```

Clona um repositório do GitHub.

```bash
gh repo view
```

Exibe informações sobre o repositório atual.

```bash
gh repo view --web
```

Abre o repositório atual no navegador.

### Issues

```bash
gh issue list
```

Lista as Issues do repositório.

```bash
gh issue create
```

Cria uma nova Issue.

```bash
gh issue view NUMERO
```

Exibe uma Issue específica.

```bash
gh issue close NUMERO
```

Fecha uma Issue.

```bash
gh issue reopen NUMERO
```

Reabre uma Issue fechada.

### Pull Requests

```bash
gh pr list
```

Lista os Pull Requests do repositório.

```bash
gh pr create
```

Cria um novo Pull Request.

```bash
gh pr view NUMERO
```

Exibe um Pull Request específico.

```bash
gh pr checkout NUMERO
```

Baixa e muda para a branch de um Pull Request.

```bash
gh pr merge NUMERO
```

Faz o merge de um Pull Request.

```bash
gh pr close NUMERO
```

Fecha um Pull Request.

### GitHub Actions

```bash
gh workflow list
```

Lista os workflows configurados no repositório.

```bash
gh workflow run NOME_DO_WORKFLOW
```

Executa manualmente um workflow.

```bash
gh run list
```

Lista as execuções recentes dos workflows.

```bash
gh run view ID
```

Exibe informações sobre uma execução específica.

```bash
gh run view ID --log
```

Exibe os logs de uma execução.

```bash
gh run cancel ID
```

Cancela uma execução em andamento.

## Fluxo básico

```bash
git clone URL_DO_REPOSITORIO
```

Baixa o projeto do GitHub.

```bash
cd cnum
```

Entra no diretório do projeto.

```bash
git switch -c nome-da-branch
```

Cria uma branch para trabalhar em uma alteração.

```bash
git status
```

Verifica as alterações realizadas.

```bash
git add .
```

Adiciona as alterações ao staging.

```bash
git commit -m "mensagem"
```

Registra as alterações em um commit.

```bash
git push -u origin nome-da-branch
```

Envia a branch para o GitHub.

Para atualizar a branch principal:

```bash
git switch main
```

Muda para a branch `main`.

```bash
git pull origin main
```

Atualiza a `main` com as alterações do GitHub.

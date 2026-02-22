# SITE-MARKETING-COMPLETO

Este projeto contém o Hub de Marketing da PRONIX, organizado de forma profissional.

## Estrutura de Pastas

- `/assets`: Contém arquivos estáticos.
  - `/css`: Estilos globais (`style.css`).
  - `/js`: Scripts globais (`main.js`).
  - `/images`: Imagens do projeto.
- `/templates`: Todos os arquivos HTML das páginas.
- `.gitignore`: Configuração para o Git ignorar arquivos desnecessários.

## Como Executar Localmente

Você pode abrir o projeto usando o servidor nativo do Python:

1. Abra o terminal na pasta raiz do projeto.
2. Execute o comando:
   ```bash
   python3 -m http.server 8000
   ```
3. No navegador, acesse: `http://localhost:8000/templates/index.html`

## Como subir para o GitHub

Para subir este projeto para o seu repositório no GitHub:

1. Crie um novo repositório vazio no seu site do GitHub.
2. Copie a URL do repositório (ex: `https://github.com/seu-usuario/seu-repositorio.git`).
3. No seu terminal (dentro desta pasta), execute:
   ```bash
   git remote add origin SUA_URL_DO_GITHUB
   git branch -M main
   git push -u origin main
   ```

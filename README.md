<p align="right">
    <a href="readme/readme-en.md">🇬🇧 English</a> |
    <a href="readme/readme-es.md">🇪🇸 Español</a>
</p>

<p align="center">
    <img src="https://placehold.co/150x150/2d0553/00ffff?text=TelecomX" align="center" width="30%">
</p>
<p align="center"><h1 align="center">TELECOMX2</h1></p>
<p align="center">
    <em>Libere insights, impulsione inovação, preveja sucesso!</em>
</p>
<p align="center">
    <a href="https://linkedin.com/in/cauasantoslt" target=_blank><img src="https://img.shields.io/badge/Meu%20Perfil-LinkedIn-00fff2?style=default&logo=linkedin&logoColor=00fff2"></a>
    <img src="https://img.shields.io/github/last-commit/cauasantoslt/telecomX2?style=default&logo=git&logoColor=white&color=00fff2" alt="last-commit">
    <img src="https://img.shields.io/github/languages/top/cauasantoslt/telecomX2?style=default&color=00fff2" alt="repo-top-language">
    <img src="https://img.shields.io/github/languages/count/cauasantoslt/telecomX2?style=default&color=00fff2" alt="repo-language-count">
</p>
<p align="center"><!-- opção padrão, sem badges de dependências. -->
</p>
<p align="center">
    <!-- opção padrão, sem badges de dependências. -->
</p>
<br>

## 🔗 Índice

- [📍 Visão Geral](#-visão-geral)
- [👾 Funcionalidades](#-funcionalidades)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
  - [📂 Índice do Projeto](#-índice-do-projeto)
- [🚀 Primeiros Passos](#-primeiros-passos)
  - [☑️ Pré-requisitos](#-pré-requisitos)
  - [⚙️ Instalação](#-instalação)
  - [🤖 Uso](#-uso)
  - [🧪 Testes](#-testes)
- [📌 Roadmap do Projeto](#-roadmap-do-projeto)
- [🔰 Contribuindo](#-contribuindo)
- [🎗 Licença](#-licença)
- [🙌 Agradecimentos](#-agradecimentos)

---

## 📍 Visão Geral

TelecomX2 é um projeto inovador que simplifica a extração de dados e aprimora a visualização da estrutura do projeto. Ele agiliza a obtenção de informações para análise e oferece uma ferramenta amigável de árvore de diretórios para fácil navegação. Ideal para desenvolvedores que buscam localizar arquivos e entender o código de forma eficiente, o TelecomX2 otimiza o fluxo de trabalho e aumenta a produtividade.

---

## 👾 Funcionalidades

|     |     Funcionalidade      | Resumo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :-- | :---------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ⚙️  |     **Arquitetura**     | <ul><li>Utiliza arquitetura modular para melhorar a manutenção e escalabilidade.</li><li>Emprega o <code>app.py</code> para orquestrar um aplicativo preditivo de churn com tema futurista usando <code>Streamlit</code>.</li><li>Integra diversos componentes para criar uma experiência envolvente e informativa dentro da arquitetura do projeto TelecomX.</li></ul>                                                                                                                                              |
| 🔩  | **Qualidade do Código** | <ul><li>Segue boas práticas de desenvolvimento Python para legibilidade e manutenção.</li><li>Inclui testes unitários com <code>pytest</code> para garantir confiabilidade.</li><li>Utiliza <code>Joblib</code> para persistência de modelos e <code>Imbalanced-learn</code> para tratar conjuntos de dados desbalanceados.</li></ul>                                                                                                                                                                                |
| 📄  |    **Documentação**     | <ul><li>Melhora a visualização da estrutura do projeto com o arquivo <code>readme-en</code>, auxiliando desenvolvedores a entenderem a arquitetura do código.</li><li>Facilita o gerenciamento de dependências via <code>requirements.txt</code>.</li><li>Traduz a documentação do projeto para espanhol com o arquivo <code>readme-es</code>.</li></ul>                                                                                                                                                             |
| 🔌  |     **Integrações**     | <ul><li>Integra <code>Streamlit</code>, <code>Pandas</code>, <code>Scikit-learn</code>, <code>Plotly</code>, <code>Joblib</code> e <code>Imbalanced-learn</code> para funcionalidade completa.</li><li>Utiliza <code>app.py</code> para carregar e pré-processar dados, exibir métricas de status do sistema e fornecer previsões de churn em tempo real.</li><li>Integra <code>salvar_modelo.py</code> para persistir dados pré-processados, treinar um modelo Random Forest e salvar arquivos de modelo.</li></ul> |
| 🧩  |    **Modularidade**     | <ul><li>Garante modularidade na arquitetura para fácil manutenção e futuras melhorias.</li><li>Separa responsabilidades utilizando arquivos diferentes para funcionalidades específicas como extração de dados, treinamento de modelo e orquestração da aplicação.</li><li>Estimula reuso e escalabilidade do código por meio de componentes modulares.</li></ul>                                                                                                                                                    |
| 🧪  |       **Testes**        | <ul><li>Inclui testes unitários com <code>pytest</code> para validar funcionalidades dos componentes.</li><li>Garante confiabilidade e robustez do código com estratégias de testes abrangentes.</li><li>Testa processamento de dados, treinamento de modelo e funcionalidades da aplicação para manter alta qualidade do código.</li></ul>                                                                                                                                                                          |
| ⚡️ |     **Performance**     | <ul><li>Otimiza performance utilizando bibliotecas eficientes como <code>Pandas</code> e <code>Scikit-learn</code> para processamento de dados e treinamento de modelos.</li><li>Utiliza <code>Joblib</code> para persistência de modelos, acelerando previsões.</li><li>Garante previsões de churn em tempo real para novos clientes com baixa latência.</li></ul>                                                                                                                                                  |

---

## 📁 Estrutura do Projeto

```sh
└── telecomX2/
    ├── README.md
    ├── TelecomX_2ipynb
    ├── app
    │   ├── app.py
    │   ├── dados_tratados.csv
    │   ├── feature_columns.pkl
    │   ├── random_forest_model.pkl
    │   ├── requirements.txt
    │   ├── salvar_modelo.py
    │   └── scaler.pkl
    ├── data
    │   └── dados_tratados.csv
    └── readme
        ├── readm-en
        └── readme-es
```

### 📂 Índice do Projeto

<details open>
    <summary><b><code>TELECOMX2/</code></b></summary>
    <details> <!-- __root__ Submodule -->
        <summary><b>__root__</b></summary>
        <blockquote>
            <table>
            <tr>
                <td><b><a href='https://github.com/cauasantoslt/telecomX2/blob/master/TelecomX_2ipynb'>TelecomX_2ipynb</a></b></td>
                <td>- O arquivo de código TelecomX_2ipynb na estrutura do projeto é focado na extração de dados<br>- Ele desempenha papel crucial na obtenção e processamento de informações relevantes para análise dentro da arquitetura do código.</td>
            </tr>
            </table>
        </blockquote>
    </details>
    <details> <!-- readme Submodule -->
        <summary><b>readme</b></summary>
        <blockquote>
            <table>
            <tr>
                <td><b><a href='https://github.com/cauasantoslt/telecomX2/blob/master/readme/readm-en'>readm-en</a></b></td>
                <td>Melhora a documentação do projeto traduzindo o arquivo README para Inglês.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/cauasantoslt/telecomX2/blob/master/readme/readme-es'>readme-es</a></b></td>
                <td>Melhora a documentação do projeto traduzindo o arquivo README para espanhol.</td>
            </tr>
            </table>
        </blockquote>
    </details>
    <details> <!-- app Submodule -->
        <summary><b>app</b></summary>
        <blockquote>
            <table>
            <tr>
                <td><b><a href='https://github.com/cauasantoslt/telecomX2/blob/master/app/app.py'>app.py</a></b></td>
                <td>- O arquivo <code>app.py</code> orquestra um aplicativo preditivo de churn com tema futurista usando Streamlit<br>- Ele carrega e pré-processa dados, exibe métricas de status do sistema, analisa o impacto de variáveis críticas no churn, fornece visualizações interativas e oferece previsões de churn em tempo real para novos clientes<br>- O arquivo integra diversos componentes para criar uma experiência envolvente e informativa dentro da arquitetura do projeto TelecomX.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/cauasantoslt/telecomX2/blob/master/app/requirements.txt'>requirements.txt</a></b></td>
                <td>- Facilita o gerenciamento de dependências do projeto especificando as bibliotecas necessárias para a aplicação<br>- O arquivo garante integração perfeita de ferramentas essenciais como Streamlit, Pandas, Scikit-learn, Plotly, Joblib e Imbalanced-learn.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/cauasantoslt/telecomX2/blob/master/app/salvar_modelo.py'>salvar_modelo.py</a></b></td>
                <td>- Persiste dados pré-processados, treina um modelo Random Forest e salva arquivos de modelo<br>- O código balanceia dados, padroniza variáveis numéricas e trata valores ausentes<br>- Ele carrega dados, codifica variáveis categóricas, divide dados e ajusta o modelo<br>- Por fim, salva o modelo treinado, scaler e colunas de features para uso futuro.</td>
            </tr>
            </table>
        </blockquote>
    </details>
</details>

---

## 🚀 Primeiros Passos

### ☑️ Pré-requisitos

Antes de começar com o telecomX2, certifique-se de que seu ambiente de execução atende aos seguintes requisitos:

- **Linguagem de Programação:** Python
- **Gerenciador de Pacotes:** Pip

### ⚙️ Instalação

Instale o telecomX2 usando um dos métodos abaixo:

**Construir a partir do código-fonte:**

1. Clone o repositório telecomX2:

```sh
❯ git clone https://github.com/cauasantoslt/telecomX2
```

2. Navegue até o diretório do projeto:

```sh
❯ cd telecomX2
```

3. Instale as dependências do projeto:

**Usando `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r app/requirements.txt
```

### 🤖 Uso

Execute o telecomX2 usando o comando abaixo:
**Usando `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```

### 🧪 Testes

Execute a suíte de testes com o comando abaixo:
**Usando `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```

---

## 📌 Roadmap do Projeto

- [x] **`Tarefa 1`**: <strike>Implementar funcionalidade um.</strike>
- [ ] **`Tarefa 2`**: Implementar funcionalidade dois.
- [ ] **`Tarefa 3`**: Implementar funcionalidade três.

---

## 🔰 Contribuindo

- **💬 [Participe das Discussões](https://github.com/cauasantoslt/telecomX2/discussions)**: Compartilhe suas ideias, dê feedback ou tire dúvidas.
- **🐛 [Reporte Problemas](https://github.com/cauasantoslt/telecomX2/issues)**: Envie bugs encontrados ou registre solicitações de funcionalidades para o projeto `telecomX2`.
- **💡 [Envie Pull Requests](https://github.com/cauasantoslt/telecomX2/blob/main/CONTRIBUTING.md)**: Revise PRs abertos e envie seus próprios PRs.

<details closed>
<summary>Diretrizes de Contribuição</summary>

1. **Faça um Fork do Repositório**: Comece fazendo um fork do repositório para sua conta do github.
2. **Clone Localmente**: Clone o repositório forkado para sua máquina local usando um cliente git.
   ```sh
   git clone https://github.com/cauasantoslt/telecomX2
   ```
3. **Crie uma Nova Branch**: Sempre trabalhe em uma nova branch, dando um nome descritivo.
   ```sh
   git checkout -b nova-funcionalidade-x
   ```
4. **Faça Suas Alterações**: Desenvolva e teste suas alterações localmente.
5. **Faça o Commit das Alterações**: Faça commits com mensagens claras descrevendo suas atualizações.
   ```sh
   git commit -m 'Implementada nova funcionalidade x.'
   ```
6. **Envie para o github**: Envie as alterações para seu repositório forkado.
   ```sh
   git push origin nova-funcionalidade-x
   ```
7. **Envie um Pull Request**: Crie um PR para o repositório original do projeto. Descreva claramente as alterações e suas motivações.
8. **Revisão**: Após a revisão e aprovação do seu PR, ele será mesclado à branch principal. Parabéns pela contribuição!
</details>

<details closed>
<summary>Gráfico de Contribuidores</summary>
<br>
<p align="left">
   <a href="https://github.com{/cauasantoslt/telecomX2/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=cauasantoslt/telecomX2">
   </a>
</p>
</details>

---

## 🎗 Licença

Este projeto é distribuído sob uma licença didática e sem fins lucrativos, desenvolvida por [Cauã Santos](https://github.com/cauasantoslt). O objetivo é promover o aprendizado, compartilhamento de conhecimento e uso acadêmico. Qualquer uso comercial é proibido.

Para mais informações, acesse o [GitHub de Cauã Santos](https://github.com/cauasantoslt).

---

## 🙌 Agradecimentos

Agradeço primeiramente a Deus, à minha família e à minha namorada por todo o apoio, carinho e incentivo durante essa jornada.

> "Seja você quem for, seja qual for a posição social que você tenha na vida, a mais alta ou a mais baixa, tenha sempre como meta muita força, muita determinação e sempre faça tudo com muito amor e com muita fé em Deus, que um dia você chega lá. De alguma maneira você chega lá."
>
> Ayrton Senna.

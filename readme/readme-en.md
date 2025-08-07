<p align="center">
    <img src="https://placehold.co/150x150/2d0553/00ffff?text=TelecomX" align="center" width="30%">
</p>
<p align="center"><h1 align="center">TELECOMX2</h1></p>
<p align="center">
    <em>Unlock insights, drive innovation, predict success!</em>
</p>
<p align="center">
    <a href="https://linkedin.com/in/cauasantoslt" target=_blank><img src="https://img.shields.io/badge/My%20Profile-LinkedIn-00fff2?style=default&logo=linkedin&logoColor=00fff2"></a>
    <img src="https://img.shields.io/github/last-commit/cauasantoslt/telecomX2?style=default&logo=git&logoColor=white&color=00fff2" alt="last-commit">
    <img src="https://img.shields.io/github/languages/top/cauasantoslt/telecomX2?style=default&color=00fff2" alt="repo-top-language">
    <img src="https://img.shields.io/github/languages/count/cauasantoslt/telecomX2?style=default&color=00fff2" alt="repo-language-count">
</p>
<br>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#-usage)
  - [🧪 Tests](#-tests)
- [📌 Roadmap](#-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgements](#-acknowledgements)

---

## 📍 Overview

TelecomX2 is an innovative project that simplifies data extraction and enhances project structure visualization. It streamlines information gathering for analysis and offers a user-friendly directory tree tool for easy navigation. Ideal for developers seeking to locate files and understand code efficiently, TelecomX2 optimizes workflow and boosts productivity.

---

## 👾 Features

|     |      Feature      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :-- | :---------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Uses modular architecture for better maintenance and scalability.</li><li>Employs <code>app.py</code> to orchestrate a futuristic-themed churn prediction app using <code>Streamlit</code>.</li><li>Integrates various components to create an engaging and informative experience within the TelecomX project architecture.</li></ul>                                                                                                                                   |
| 🔩  | **Code Quality**  | <ul><li>Follows Python development best practices for readability and maintainability.</li><li>Includes unit tests with <code>pytest</code> for reliability.</li><li>Uses <code>Joblib</code> for model persistence and <code>Imbalanced-learn</code> to handle imbalanced datasets.</li></ul>                                                                                                                                                                                   |
| 📄  | **Documentation** | <ul><li>Improves project structure visualization with the <code>readme-en</code> file, helping developers understand code architecture.</li><li>Facilitates dependency management via <code>requirements.txt</code>.</li><li>Translates project documentation to Spanish with the <code>readme-es</code> file.</li></ul>                                                                                                                                                         |
| 🔌  | **Integrations**  | <ul><li>Integrates <code>Streamlit</code>, <code>Pandas</code>, <code>Scikit-learn</code>, <code>Plotly</code>, <code>Joblib</code>, and <code>Imbalanced-learn</code> for full functionality.</li><li>Uses <code>app.py</code> to load and preprocess data, display system status metrics, and provide real-time churn predictions.</li><li>Integrates <code>salvar_modelo.py</code> to persist preprocessed data, train a Random Forest model, and save model files.</li></ul> |
| 🧩  |  **Modularity**   | <ul><li>Ensures modularity in architecture for easy maintenance and future improvements.</li><li>Separates responsibilities using different files for specific functionalities like data extraction, model training, and app orchestration.</li><li>Encourages code reuse and scalability through modular components.</li></ul>                                                                                                                                                  |
| 🧪  |    **Testing**    | <ul><li>Includes unit tests with <code>pytest</code> to validate component functionalities.</li><li>Ensures code reliability and robustness with comprehensive testing strategies.</li><li>Tests data processing, model training, and app features to maintain high code quality.</li></ul>                                                                                                                                                                                      |
| ⚡️ |  **Performance**  | <ul><li>Optimizes performance using efficient libraries like <code>Pandas</code> and <code>Scikit-learn</code> for data processing and model training.</li><li>Uses <code>Joblib</code> for model persistence, speeding up predictions.</li><li>Provides real-time churn predictions for new clients with low latency.</li></ul>                                                                                                                                                 |

---

## 📁 Project Structure

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
        ├── readme-en
        └── readme-es
```

### 📂 Project Index

<details open>
    <summary><b><code>TELECOMX2/</code></b></summary>
    <details> <!-- __root__ Submodule -->
        <summary><b>__root__</b></summary>
        <blockquote>
            <table>
            <tr>
                <td><b><a href='https://github.com/cauasantoslt/telecomX2/blob/master/TelecomX_2ipynb'>TelecomX_2ipynb</a></b></td>
                <td>- The TelecomX_2ipynb code file in the project structure focuses on data extraction<br>- It plays a crucial role in obtaining and processing relevant information for analysis within the code architecture.</td>
            </tr>
            </table>
        </blockquote>
    </details>
    <details> <!-- readme Submodule -->
        <summary><b>readme</b></summary>
        <blockquote>
            <table>
            <tr>
                <td><b><a href='https://github.com/cauasantoslt/telecomX2/blob/master/readme/readme-en'>readme-en</a></b></td>
                <td>- Improves project structure visualization by generating a comprehensive directory tree<br>- This tool simplifies navigation and understanding of code architecture, helping developers efficiently locate files and directories.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/cauasantoslt/telecomX2/blob/master/readme/readme-es'>readme-es</a></b></td>
                <td>Improves project documentation by translating the README file to Spanish.</td>
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
                <td>- The <code>app.py</code> file orchestrates a futuristic-themed churn prediction app using Streamlit<br>- It loads and preprocesses data, displays system status metrics, analyzes the impact of critical variables on churn, provides interactive visualizations, and offers real-time churn predictions for new clients<br>- The file integrates various components to create an engaging and informative experience within the TelecomX project architecture.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/cauasantoslt/telecomX2/blob/master/app/requirements.txt'>requirements.txt</a></b></td>
                <td>- Facilitates project dependency management by specifying required libraries for the application<br>- The file ensures seamless integration of essential tools like Streamlit, Pandas, Scikit-learn, Plotly, Joblib, and Imbalanced-learn.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/cauasantoslt/telecomX2/blob/master/app/salvar_modelo.py'>salvar_modelo.py</a></b></td>
                <td>- Persists preprocessed data, trains a Random Forest model, and saves model files<br>- The code balances data, standardizes numerical variables, and handles missing values<br>- It loads data, encodes categorical variables, splits data, and fits the model<br>- Finally, it saves the trained model, scaler, and feature columns for future use.</td>
            </tr>
            </table>
        </blockquote>
    </details>
</details>

---

## 🚀 Getting Started

### ☑️ Prerequisites

Before starting with telecomX2, make sure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip

### ⚙️ Installation

Install telecomX2 using one of the methods below:

**Build from source:**

1. Clone the telecomX2 repository:

```sh
❯ git clone https://github.com/cauasantoslt/telecomX2
```

2. Navigate to the project directory:

```sh
❯ cd telecomX2
```

3. Install project dependencies:

**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r app/requirements.txt
```

### 🤖 Usage

Run telecomX2 using the command below:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```

### 🧪 Tests

Run the test suite with the command below:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```

---

## 📌 Roadmap

- [x] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join Discussions](https://github.com/cauasantoslt/telecomX2/discussions)**: Share ideas, give feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/cauasantoslt/telecomX2/issues)**: Submit bugs or feature requests for the `telecomX2` project.
- **💡 [Submit Pull Requests](https://github.com/cauasantoslt/telecomX2/blob/main/CONTRIBUTING.md)**: Review open PRs and submit your own.

<details closed>
<summary>Contribution Guidelines</summary>

1. **Fork the Repository**: Start by forking the repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/cauasantoslt/telecomX2
   ```
3. **Create a New Branch**: Always work on a new branch with a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with clear messages describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push your changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR to the original project repository. Clearly describe the changes and motivations.
8. **Review**: After review and approval, your PR will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributors Graph</summary>
<br>
<p align="left">
   <a href="https://github.com/cauasantoslt/telecomX2/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=cauasantoslt/telecomX2">
   </a>
</p>
</details>

---

## 🎗 License

This project is distributed under a didactic and non-profit license, developed by [Cauã Santos](https://github.com/cauasantoslt). The goal is to promote learning, knowledge sharing, and academic use. Any commercial use is prohibited.

For more information, visit [Cauã Santos' GitHub](https://github.com/cauasantoslt).

---

## 🙌 Acknowledgements

I thank God, my family, and my girlfriend for all the support, affection, and encouragement throughout this journey.

> "No matter who you are, no matter what social position you have in life, the highest or the lowest, always have as your goal a lot of strength, a lot of determination, and always do everything with a lot of love and a lot of faith in God, that one day you will get there. Somehow, you will get there."
>
> Ayrton Senna.

---

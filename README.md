<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">TELECOMX2</h1></p>
<p align="center">
	<em>Unleash insights, power innovation, predict success!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/cauasantoslt/telecomX2?style=default&logo=opensourceinitiative&logoColor=white&color=00fff2" alt="license">
	<img src="https://img.shields.io/github/last-commit/cauasantoslt/telecomX2?style=default&logo=git&logoColor=white&color=00fff2" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/cauasantoslt/telecomX2?style=default&color=00fff2" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/cauasantoslt/telecomX2?style=default&color=00fff2" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
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
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

TelecomX2 is a cutting-edge project that simplifies data extraction and enhances project structure visualization. It streamlines information retrieval for analysis and offers a user-friendly directory tree tool for easy navigation. Ideal for developers seeking efficient file location and codebase understanding, TelecomX2 optimizes workflow and boosts productivity.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes a modular architecture design to enhance maintainability and scalability.</li><li>Employs <code>app.py</code> to orchestrate a futuristic-themed predictive churn analysis application using <code>Streamlit</code>.</li><li>Integrates various components to create an engaging and informative user experience within the TelecomX project architecture.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Follows best practices in Python development for readability and maintainability.</li><li>Includes unit tests using <code>pytest</code> to ensure code reliability.</li><li>Utilizes <code>Joblib</code> for model persistence and <code>Imbalanced-learn</code> for handling imbalanced datasets.</li></ul> |
| 📄 | **Documentation** | <ul><li>Enhances project structure visualization with the <code>readme-en</code> file, aiding developers in understanding the codebase architecture.</li><li>Facilitates dependencies management through the <code>requirements.txt</code> file.</li><li>Translates project documentation into Spanish with the <code>readme-es</code> file.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates <code>Streamlit</code>, <code>Pandas</code>, <code>Scikit-learn</code>, <code>Plotly</code>, <code>Joblib</code>, and <code>Imbalanced-learn</code> for seamless functionality.</li><li>Utilizes <code>app.py</code> to load and preprocess data, display system status metrics, and provide real-time churn predictions.</li><li>Integrates <code>salvar_modelo.py</code> to persist pre-processed data, train a Random Forest model, and save model files.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Ensures modularity in the architecture design for easy maintenance and future enhancements.</li><li>Separates concerns by utilizing different files for specific functionalities like data extraction, model training, and application orchestration.</li><li>Encourages code reusability and scalability through modular components.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes unit tests using <code>pytest</code> to validate the functionality of different components.</li><li>Ensures code reliability and robustness through comprehensive testing strategies.</li><li>Tests data processing, model training, and application functionality to maintain high code quality.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimizes performance by utilizing efficient libraries like <code>Pandas</code> and <code>Scikit-learn</code> for data processing and model training.</li><li>Utilizes <code>Joblib</code> for model persistence to enhance prediction speed.</li><li>Ensures real-time churn predictions for new customers with minimal latency.</li></ul> |

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
        ├── readm-en
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
				<td>- The code file TelecomX_2ipynb in the project structure is focused on data extraction<br>- It plays a crucial role in retrieving and processing relevant information for further analysis within the codebase architecture.</td>
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
				<td>- Enhances project structure visualization by generating a comprehensive directory tree<br>- This tool simplifies navigation and understanding of the codebase architecture, aiding developers in efficiently locating files and directories.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/cauasantoslt/telecomX2/blob/master/readme/readme-es'>readme-es</a></b></td>
				<td>Improve project documentation by translating the README file into Spanish.</td>
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
				<td>- The code file `app.py` orchestrates a futuristic-themed predictive churn analysis application using Streamlit<br>- It loads and preprocesses data, displays system status metrics, analyzes critical variables' impact on churn, provides interactive visualizations, and offers real-time churn predictions for new customers<br>- The file integrates various components to create an engaging and informative user experience within the TelecomX project architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/cauasantoslt/telecomX2/blob/master/app/requirements.txt'>requirements.txt</a></b></td>
				<td>- Facilitates project dependencies management by specifying required libraries for the application<br>- The file ensures seamless integration of essential tools like Streamlit, Pandas, Scikit-learn, Plotly, Joblib, and Imbalanced-learn.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/cauasantoslt/telecomX2/blob/master/app/salvar_modelo.py'>salvar_modelo.py</a></b></td>
				<td>- Persist pre-processed data, train a Random Forest model, and save model files<br>- The code balances data, standardizes numeric variables, and handles missing values<br>- It loads data, encodes categorical features, splits data, and fits the model<br>- Finally, it saves the trained model, scaler, and feature columns for future use.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with telecomX2, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


### ⚙️ Installation

Install telecomX2 using one of the following methods:

**Build from source:**

1. Clone the telecomX2 repository:
```sh
❯ git clone https://github.com/cauasantoslt/telecomX2
```

2. Navigate to the project directory:
```sh
❯ cd telecomX2
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r app/requirements.txt
```




### 🤖 Usage
Run telecomX2 using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


### 🧪 Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/cauasantoslt/telecomX2/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/cauasantoslt/telecomX2/issues)**: Submit bugs found or log feature requests for the `telecomX2` project.
- **💡 [Submit Pull Requests](https://github.com/cauasantoslt/telecomX2/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/cauasantoslt/telecomX2
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/cauasantoslt/telecomX2/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=cauasantoslt/telecomX2">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---

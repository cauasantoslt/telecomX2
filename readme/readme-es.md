<p align="center">
    <img src="https://placehold.co/150x150/2d0553/00ffff?text=TelecomX" align="center" width="30%">
</p>
<p align="center"><h1 align="center">TELECOMX2</h1></p>
<p align="center">
    <em>¡Libera insights, impulsa innovación, predice el éxito!</em>
</p>
<p align="center">
    <a href="https://linkedin.com/in/cauasantoslt" target=_blank><img src="https://img.shields.io/badge/Mi%20Perfil-LinkedIn-00fff2?style=default&logo=linkedin&logoColor=00fff2"></a>
    <img src="https://img.shields.io/github/last-commit/cauasantoslt/telecomX2?style=default&logo=git&logoColor=white&color=00fff2" alt="last-commit">
    <img src="https://img.shields.io/github/languages/top/cauasantoslt/telecomX2?style=default&color=00fff2" alt="repo-top-language">
    <img src="https://img.shields.io/github/languages/count/cauasantoslt/telecomX2?style=default&color=00fff2" alt="repo-language-count">
</p>
<br>

## 🔗 Índice

- [📍 Visión General](#-visión-general)
- [👾 Funcionalidades](#-funcionalidades)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
  - [📂 Índice del Proyecto](#-índice-del-proyecto)
- [🚀 Primeros Pasos](#-primeros-pasos)
  - [☑️ Requisitos Previos](#-requisitos-previos)
  - [⚙️ Instalación](#-instalación)
  - [🤖 Uso](#-uso)
  - [🧪 Pruebas](#-pruebas)
- [📌 Roadmap](#-roadmap)
- [🔰 Contribuyendo](#-contribuyendo)
- [🎗 Licencia](#-licencia)
- [🙌 Agradecimientos](#-agradecimientos)

---

## 📍 Visión General

TelecomX2 es un proyecto innovador que simplifica la extracción de datos y mejora la visualización de la estructura del proyecto. Agiliza la obtención de información para el análisis y ofrece una herramienta amigable de árbol de directorios para una navegación fácil. Ideal para desarrolladores que buscan localizar archivos y entender el código de manera eficiente, TelecomX2 optimiza el flujo de trabajo y aumenta la productividad.

---

## 👾 Funcionalidades

|     |     Funcionalidad     | Resumen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :-- | :-------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ⚙️  |   **Arquitectura**    | <ul><li>Utiliza arquitectura modular para mejorar el mantenimiento y la escalabilidad.</li><li>Emplea <code>app.py</code> para orquestar una aplicación predictiva de churn con temática futurista usando <code>Streamlit</code>.</li><li>Integra varios componentes para crear una experiencia envolvente e informativa dentro de la arquitectura del proyecto TelecomX.</li></ul>                                                                                                                                       |
| 🔩  | **Calidad de Código** | <ul><li>Sigue buenas prácticas de desarrollo en Python para legibilidad y mantenimiento.</li><li>Incluye pruebas unitarias con <code>pytest</code> para garantizar confiabilidad.</li><li>Utiliza <code>Joblib</code> para persistencia de modelos y <code>Imbalanced-learn</code> para tratar conjuntos de datos desbalanceados.</li></ul>                                                                                                                                                                               |
| 📄  |   **Documentación**   | <ul><li>Mejora la visualización de la estructura del proyecto con el archivo <code>readme-en</code>, ayudando a los desarrolladores a entender la arquitectura del código.</li><li>Facilita la gestión de dependencias mediante <code>requirements.txt</code>.</li><li>Traduce la documentación del proyecto al inglés con el archivo <code>readme-en</code>.</li></ul>                                                                                                                                                   |
| 🔌  |   **Integraciones**   | <ul><li>Integra <code>Streamlit</code>, <code>Pandas</code>, <code>Scikit-learn</code>, <code>Plotly</code>, <code>Joblib</code> y <code>Imbalanced-learn</code> para funcionalidad completa.</li><li>Utiliza <code>app.py</code> para cargar y preprocesar datos, mostrar métricas de estado del sistema y proporcionar predicciones de churn en tiempo real.</li><li>Integra <code>salvar_modelo.py</code> para persistir datos preprocesados, entrenar un modelo Random Forest y guardar archivos de modelo.</li></ul> |
| 🧩  |    **Modularidad**    | <ul><li>Garantiza modularidad en la arquitectura para fácil mantenimiento y futuras mejoras.</li><li>Separa responsabilidades utilizando archivos diferentes para funcionalidades específicas como extracción de datos, entrenamiento de modelos y orquestación de la aplicación.</li><li>Fomenta la reutilización y escalabilidad del código mediante componentes modulares.</li></ul>                                                                                                                                   |
| 🧪  |      **Pruebas**      | <ul><li>Incluye pruebas unitarias con <code>pytest</code> para validar funcionalidades de los componentes.</li><li>Garantiza confiabilidad y robustez del código con estrategias de pruebas integrales.</li><li>Prueba el procesamiento de datos, el entrenamiento de modelos y las funcionalidades de la aplicación para mantener alta calidad de código.</li></ul>                                                                                                                                                      |
| ⚡️ |    **Rendimiento**    | <ul><li>Optimiza el rendimiento utilizando bibliotecas eficientes como <code>Pandas</code> y <code>Scikit-learn</code> para procesamiento de datos y entrenamiento de modelos.</li><li>Utiliza <code>Joblib</code> para persistencia de modelos, acelerando las predicciones.</li><li>Garantiza predicciones de churn en tiempo real para nuevos clientes con baja latencia.</li></ul>                                                                                                                                    |

---

## 📁 Estructura del Proyecto

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

### 📂 Índice del Proyecto

<details open>
    <summary><b><code>TELECOMX2/</code></b></summary>
    <details> <!-- __root__ Submodule -->
        <summary><b>__root__</b></summary>
        <blockquote>
            <table>
            <tr>
                <td><b><a href='https://github.com/cauasantoslt/telecomX2/blob/master/TelecomX_2ipynb'>TelecomX_2ipynb</a></b></td>
                <td>- El archivo de código TelecomX_2ipynb en la estructura del proyecto está enfocado en la extracción de datos<br>- Desempeña un papel crucial en la obtención y procesamiento de información relevante para el análisis dentro de la arquitectura del código.</td>
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
                <td>Mejora la documentación del proyecto traduciendo el archivo README al inglés.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/cauasantoslt/telecomX2/blob/master/readme/readme-es'>readme-es</a></b></td>
                <td>Mejora la documentación del proyecto traduciendo el archivo README al español.</td>
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
                <td>- El archivo <code>app.py</code> orquesta una aplicación predictiva de churn con temática futurista usando Streamlit<br>- Carga y preprocesa datos, muestra métricas de estado del sistema, analiza el impacto de variables críticas en el churn, proporciona visualizaciones interactivas y ofrece predicciones de churn en tiempo real para nuevos clientes<br>- El archivo integra varios componentes para crear una experiencia envolvente e informativa dentro de la arquitectura del proyecto TelecomX.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/cauasantoslt/telecomX2/blob/master/app/requirements.txt'>requirements.txt</a></b></td>
                <td>- Facilita la gestión de dependencias del proyecto especificando las bibliotecas necesarias para la aplicación<br>- El archivo garantiza la integración perfecta de herramientas esenciales como Streamlit, Pandas, Scikit-learn, Plotly, Joblib e Imbalanced-learn.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/cauasantoslt/telecomX2/blob/master/app/salvar_modelo.py'>salvar_modelo.py</a></b></td>
                <td>- Persiste datos preprocesados, entrena un modelo Random Forest y guarda archivos de modelo<br>- El código balancea datos, estandariza variables numéricas y trata valores faltantes<br>- Carga datos, codifica variables categóricas, divide datos y ajusta el modelo<br>- Finalmente, guarda el modelo entrenado, el scaler y las columnas de características para uso futuro.</td>
            </tr>
            </table>
        </blockquote>
    </details>
</details>

---

## 🚀 Primeros Pasos

### ☑️ Requisitos Previos

Antes de comenzar con telecomX2, asegúrate de que tu entorno de ejecución cumpla con los siguientes requisitos:

- **Lenguaje de Programación:** Python
- **Gestor de Paquetes:** Pip

### ⚙️ Instalación

Instala telecomX2 usando uno de los métodos abajo:

**Construir desde el código fuente:**

1. Clona el repositorio telecomX2:

```sh
❯ git clone https://github.com/cauasantoslt/telecomX2
```

2. Navega al directorio del proyecto:

```sh
❯ cd telecomX2
```

3. Instala las dependencias del proyecto:

**Usando `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r app/requirements.txt
```

### 🤖 Uso

Ejecuta telecomX2 usando el siguiente comando:
**Usando `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```

### 🧪 Pruebas

Ejecuta la suite de pruebas con el siguiente comando:
**Usando `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```

---

## 📌 Roadmap

- [x] **`Tarea 1`**: <strike>Implementar funcionalidad uno.</strike>
- [ ] **`Tarea 2`**: Implementar funcionalidad dos.
- [ ] **`Tarea 3`**: Implementar funcionalidad tres.

---

## 🔰 Contribuyendo

- **💬 [Participa en las discusiones](https://github.com/cauasantoslt/telecomX2/discussions)**: Comparte tus ideas, da feedback o haz preguntas.
- **🐛 [Reporta problemas](https://github.com/cauasantoslt/telecomX2/issues)**: Envía bugs encontrados o solicita funcionalidades para el proyecto `telecomX2`.
- **💡 [Envía Pull Requests](https://github.com/cauasantoslt/telecomX2/blob/main/CONTRIBUTING.md)**: Revisa PRs abiertos y envía tus propios PRs.

<details closed>
<summary>Guía de Contribución</summary>

1. **Haz un Fork del Repositorio**: Comienza haciendo un fork del repositorio en tu cuenta de GitHub.
2. **Clona Localmente**: Clona el repositorio forkeado a tu máquina local usando un cliente git.
   ```sh
   git clone https://github.com/cauasantoslt/telecomX2
   ```
3. **Crea una Nueva Rama**: Trabaja siempre en una nueva rama con un nombre descriptivo.
   ```sh
   git checkout -b nueva-funcionalidad-x
   ```
4. **Haz tus Cambios**: Desarrolla y prueba tus cambios localmente.
5. **Haz Commit de tus Cambios**: Haz commits con mensajes claros describiendo tus actualizaciones.
   ```sh
   git commit -m 'Implementada nueva funcionalidad x.'
   ```
6. **Envía a GitHub**: Envía los cambios a tu repositorio forkeado.
   ```sh
   git push origin nueva-funcionalidad-x
   ```
7. **Envía un Pull Request**: Crea un PR al repositorio original del proyecto. Describe claramente los cambios y tus motivaciones.
8. **Revisión**: Tras la revisión y aprobación, tu PR será fusionado a la rama principal. ¡Felicitaciones por tu contribución!
</details>

<details closed>
<summary>Gráfico de Contribuidores</summary>
<br>
<p align="left">
   <a href="https://github.com/cauasantoslt/telecomX2/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=cauasantoslt/telecomX2">
   </a>
</p>
</details>

---

## 🎗 Licencia

Este proyecto se distribuye bajo una licencia didáctica y sin fines de lucro, desarrollada por [Cauã Santos](https://github.com/cauasantoslt). El objetivo es promover el aprendizaje, el intercambio de conocimiento y el uso académico. Cualquier uso comercial está prohibido.

Para más información, visita el [GitHub de Cauã Santos](https://github.com/cauasantoslt).

---

## 🙌 Agradecimientos

Agradezco primeramente a Dios, a mi familia y a mi novia por todo el apoyo, cariño y ánimo durante esta jornada.

>"No importa quién seas, ni cuál sea tu posición social en la vida, la más alta o la más baja, ten siempre como meta mucha fuerza, mucha determinación y haz siempre todo con mucho amor y mucha fe en Dios, que un día llegarás. De una forma u otra, llegarás."  
>
>Ayrton Senna.

---
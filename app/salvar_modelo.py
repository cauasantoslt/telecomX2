import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE

# 1. Carregar e pré-processar os dados
# O caminho foi ajustado para o mesmo diretório
df = pd.read_csv('dados_tratados.csv')

# Removendo linhas com valores ausentes na coluna 'Churn'
df = df.dropna(subset=['Churn'])

df = df.drop(columns=['customerID', 'Contas_Diarias'])
df_encoded = pd.get_dummies(df, drop_first=True)
X = df_encoded.drop('Churn', axis=1)
y = df_encoded['Churn']

# 2. Balancear os dados
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# 3. Padronizar as variáveis numéricas
scaler = StandardScaler()
colunas_numericas = ['customer_tenure', 'account_Charges.Monthly', 'account_Charges.Total']
X_resampled[colunas_numericas] = scaler.fit_transform(X_resampled[colunas_numericas])

# 4. Treinar o modelo
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)
random_forest = RandomForestClassifier(n_estimators=100, random_state=42)
random_forest.fit(X_train, y_train)

# 5. Salvar o modelo e os outros arquivos na mesma pasta
joblib.dump(random_forest, 'random_forest_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(X_resampled.columns.tolist(), 'feature_columns.pkl')
print("Arquivos do modelo salvos com sucesso!")

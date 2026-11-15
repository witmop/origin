import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split,KFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
from catboost import CatBoostRegressor,Pool
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt



# 1. Загружаем данные
df = pd.read_csv("clean_df.csv")

# # 2. Явно удаляем столбцы, которые только навредят модели:
# # 'Model' имеет слишком много уникальных значений (это вызовет переобучение)
# # 'ID' или 'Color' не несут полезной информации для цены
cols_to_drop = ['Color', 'ID']
df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])

# # 3. Находим все оставшиеся текстовые столбцы (Make, Style, Fuel, Transmission, Drive, Wheel)
categorical_cols = df.select_dtypes(include=['object', 'string']).columns.tolist()

# # 4. Кодируем текстовые столбцы в числа (One-Hot Encoding)
# drop_first=True предотвращает дублирование информации (мультиколлинеарность)
df_encoded = pd.get_dummies(df, columns=categorical_cols, dtype=int)

# # 5. Разделяем на признаки (X) и целевую переменную (y)
X = df_encoded.drop('Price', axis=1)
y = df_encoded['Price']

# # Удаляем строки с пропусками (на всякий случай, чтобы модель не упала)
mask = X.notna().all(axis=1)
X = X[mask]
y = y[mask]

# print(f"Итоговые признаки для обучения ({X.shape[1]} шт.):", list(X.columns)[:10], "...")
# print(f"Размер данных: {X.shape}")

# # 6. Разбиваем на обучающую (80%) и валидационную (20%) выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Обучаем улучшенную модель
model = RandomForestRegressor(n_estimators=50, random_state=42, n_jobs=-1,max_features=0.3)
model.fit(X_train, y_train)

# 8. Делаем предсказания
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# 9. Выводим метрики
print("\n" + "="*45)
print("📊 РЕЗУЛЬТАТЫ МОДЕЛИ")
print("="*45)
print(f"Train MAE:      {mean_absolute_error(y_train, y_train_pred):>8.2f}")
print(f"Train MAPE:     {mean_absolute_percentage_error(y_train, y_train_pred) * 100:>7.2f}%")
print("-" * 45)
print(f"Validation MAE: {mean_absolute_error(y_test, y_test_pred):>8.2f}")
print(f"Validation MAPE:{mean_absolute_percentage_error(y_test, y_test_pred) * 100:>7.2f}%")
print("="*45)

# Бонус: посмотрим, какие признаки модель считает самыми важными
importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\n🏆 Топ-5 самых важных признаков:")
print(importances.head(5).round(4))

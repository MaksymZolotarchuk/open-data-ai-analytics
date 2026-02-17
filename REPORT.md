# REPORT

## 1. Репозиторій
- Link: https://github.com/MaksymZolotarchuk/open-data-ai-analytics
## 2. Джерело даних
- Портал відкритих даних України: https://data.gov.ua/
- Датасет: Дані щодо транспортних засобів за 2024 рік
- Формат даних: CSV
- Основні поля датасету:
  PERSON, REG_ADDR_KOATUU, OPER_CODE, OPER_NAME, D_REG, DEP_CODE, DEP,
  BRAND, MODEL, VIN, MAKE_YEAR, COLOR, KIND, BODY, PURPOSE, FUEL,
  CAPACITY, OWN_WEIGHT, TOTAL_WEIGHT, N_REG_NEW

## 3. Опис виконаної роботи
У межах проєкту було реалізовано повний цикл аналізу відкритих даних:
- завантаження датасету з data.gov.ua
- перевірка якості даних (пропуски, дублікати, типи даних)
- дослідження даних (EDA, статистика, кореляція)
- побудова графіків та візуалізацій

## 4. Реалізовані модулі
### 4.1 data_load
Файл: `src/data_load/download.py`  
Функція: завантаження CSV-файлу за прямим посиланням у папку `data/raw/`.

### 4.2 data_quality_analysis
Файл: `src/data_quality_analysis/quality.py`  
Функція: перевірка якості даних (пропуски, дублікати, типи колонок).  
Результат зберігається у `reports/data_quality_report.json`.

### 4.3 data_research
Файл: `src/data_research/research.py`  
Функція: базове дослідження даних, формування статистики та кореляцій.  
Результати:
- `reports/eda_describe.csv`
- `reports/correlation.csv`

### 4.4 visualization
Файл: `src/visualization/plots.py`  
Функція: побудова візуалізацій для числових показників.  
Результати зберігаються у `reports/figures/`.

## 5. Merge-конфлікт
Було створено дві гілки, які змінювали одну й ту саму секцію у файлі `README.md`.  
Під час merge виник конфлікт, який було вирішено вручну та зафіксовано комітом.

## 6. Інструкція запуску
### Завантаження даних
```bash
DATA_URL="(посилання на CSV з data.gov.ua)" DATA_FILENAME="vehicles_2024.csv" python -m src.data_load.download
```

### Перевірка якості даних
```bash
python -m src.data_quality_analysis.quality
```

### Дослідження даних
```bash
python -m src.data_research.research
```

### Візуалізація
```bash
python -m src.visualization.plots
```

## 7. Висновок
Отримано базові статистичні характеристики транспортних засобів за 2024 рік.
Проєкт демонструє повний pipeline роботи з відкритими даними: завантаження, перевірка,
аналіз та візуалізація.

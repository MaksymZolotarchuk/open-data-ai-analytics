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
DATA_URL="(https://data.gov.ua/dataset/06779371-308f-42d7-895e-5a39833375f0/resource/c3ffecc4-bb5c-4102-b761-6dcfeb60b4fe)" DATA_FILENAME="tz_opendata_z01012024_po01012025" python -m src.data_load.download
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

## 8. Git log
* 49089e4 (HEAD -> main, origin/main) docs: add report
* 0374534 docs: add report
* 722de3b (tag: v0.1.0) docs: add changelog
*   540438c merge: feature/visualization
|\  
| * 1e6bdce (feature/visualization) feat(visualization): add basic plots
|/  
*   3481648 fix: resolve README merge conflict
|\  
| * 3524dd6 (feature/conflict_b) docs: change conflict line (B)
* | 6987f90 (feature/conflict_a) docs: change conflict line (A)
|/  
* b769fa9 reset README before conflict demo
* 55988b0 docs: change conflict line (A)
* cac93b1 docs: add conflict marker line
*   80a4244 merge: feature/data_research
|\  
| * a63fe6a (feature/data_research) feat(data_research): add EDA outputs
* |   8162874 merge: feature/data_quality_analysis
|\ \  
| |/  
|/|   
| * 245c80a (feature/data_quality_analysis) feat(data_quality): add data quality report
|/  
*   67d20b5 merge: feature/data_load
|\  
| * c9b05f6 (feature/data_load) feat(data_load): add data download script
| * de6228d docs: add project description, data source and hypotheses
| * 959e625 chore: init structure and gitignore
|/  
* faf399d docs: add project description, data source and hypotheses
* adf1c60 chore: init project structure and gitignore
* 13463a7 add gitignore
* 9ac51b0 add data readme

# 🎵 Analiza rynku koncertów muzycznych w Polsce

Projekt przedstawia analizę danych dotyczących rynku koncertów muzycznych w Polsce z wykorzystaniem biblioteki **Plotly**. Celem analizy było przygotowanie interaktywnych wizualizacji prezentujących strukturę rynku, przychody, liczbę wydarzeń oraz zależności pomiędzy wybranymi zmiennymi.

Projekt został wykonany w formie **Jupyter Notebook** w ramach zajęć z przedmiotu **Big Data**.

---

## 📊 Zakres analizy

W projekcie wykonano:

- wczytanie i eksplorację danych,
- analizę liczby koncertów,
- analizę przychodów według miast,
- analizę zmian liczby koncertów w czasie,
- analizę cen biletów,
- analizę przychodów według typu obiektu,
- analizę zależności pomiędzy ceną biletu a wypełnieniem obiektu,
- wizualizację lokalizacji koncertów na mapie Polski,
- podsumowanie danych z wykorzystaniem subplotów.

---

## 📈 Wykorzystane wizualizacje

Projekt zawiera następujące typy wykresów:

- 📊 wykres słupkowy,
- 📈 wykres liniowy,
- 📉 histogram,
- 📦 boxplot,
- 🎯 scatter plot,
- 🗺️ mapa Polski,
- 📋 subploty (2×2).

---

## 🛠️ Wykorzystane technologie

- Pandas
- Plotly
- Jupyter Notebook

---

## 📂 Struktura projektu

```
Analiza_Koncertow/
│
├── analiza_koncertow.ipynb
├── koncerty_polska.csv
├── app.py
├── .gitignore
└── README.md
```

---

## ▶️ Uruchomienie projektu

1. Sklonuj repozytorium:

```bash
git clone https://github.com/CyprianZTL/Analiza_Koncertow.git
```

2. Przejdź do katalogu projektu:

```bash
cd Analiza_Koncertow
```

3. Zainstaluj wymagane biblioteki:

```bash
pip install pandas plotly notebook
```

4. Uruchom Jupyter Notebook:

```bash
jupyter notebook
```

5. Otwórz plik:

```
analiza_koncertow.ipynb
```

i wykonaj wszystkie komórki.

---

## 📄 Dane

Dane wykorzystane w projekcie zostały wygenerowane zgodnie z poleceniem do zadania laboratoryjnego i zapisane w pliku:

```
koncerty_polska.csv
```

Zbiór zawiera informacje o:

- mieście,
- dacie koncertu,
- gatunku muzycznym,
- typie obiektu,
- pojemności,
- liczbie sprzedanych biletów,
- cenie biletu,
- przychodzie,
- współrzędnych geograficznych.

---

## 👨‍💻 Autor

**Cyprian**

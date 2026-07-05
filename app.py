import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# WCZYTANIE DANYCH


df = pd.read_csv(
    "koncerty_polska.csv",
    parse_dates=["data"]
)

print("===== SHAPE =====")
print(df.shape)

print("\n===== HEAD =====")
print(df.head())

print("\n===== DTYPES =====")
print(df.dtypes)

print("\n===== UNIKALNE MIASTA =====")
print(df["miasto"].nunique())

print("\n===== UNIKALNE GATUNKI =====")
print(df["gatunek"].nunique())


# WYKRES SŁUPKOWY

przychody = (
    df.groupby("miasto")["przychod_pln"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig = px.bar(
    przychody,
    x="miasto",
    y="przychod_pln",
    title="Łączny przychód według miasta",
    labels={
        "miasto":"Miasto",
        "przychod_pln":"Przychód [PLN]"
    },
    color="przychod_pln",
    color_continuous_scale="Blues"
)

fig.show()

# SZEREG CZASOWY


df["miesiac"] = df["data"].dt.to_period("M").astype(str)

koncerty_miesiac = (
    df.groupby("miesiac")
    .size()
    .reset_index(name="liczba_koncertow")
)

fig = px.line(
    koncerty_miesiac,
    x="miesiac",
    y="liczba_koncertow",
    markers=True,
    title="Liczba koncertów w kolejnych miesiącach",
    labels={
        "miesiac":"Miesiąc",
        "liczba_koncertow":"Liczba koncertów"
    }
)

fig.show()


# LICZBA KONCERTÓW WG OBIEKTU


typy = (
    df.groupby(["miesiac","typ_obiektu"])
    .size()
    .reset_index(name="liczba")
)

fig = px.line(
    typy,
    x="miesiac",
    y="liczba",
    color="typ_obiektu",
    markers=True,
    title="Liczba koncertów według typu obiektu",
    labels={
        "miesiac":"Miesiąc",
        "liczba":"Liczba koncertów",
        "typ_obiektu":"Typ obiektu"
    }
)

fig.show()


# HISTOGRAM CEN BILETÓW


fig = px.histogram(
    df,
    x="cena_biletu_pln",
    nbins=50,
    title="Rozkład cen biletów",
    labels={
        "cena_biletu_pln":"Cena biletu [PLN]"
    }
)

fig.show()


# BOXPLOT PRZYCHODÓW


fig = px.box(
    df,
    x="typ_obiektu",
    y="przychod_pln",
    color="typ_obiektu",
    title="Przychód według typu obiektu",
    labels={
        "typ_obiektu":"Typ obiektu",
        "przychod_pln":"Przychód [PLN]"
    }
)

fig.show()

print("""
Wniosek:
Największe przychody generują koncerty organizowane
na stadionach oraz festiwalach.
""")

# SCATTER PLOT


df["wypelnienie"] = (
        df["bilety_sprzedane"] /
        df["pojemnosc"]
)

fig = px.scatter(
    df,
    x="cena_biletu_pln",
    y="wypelnienie",
    color="gatunek",
    size="pojemnosc",
    hover_data=["miasto", "typ_obiektu"],
    title="Cena biletu a wypełnienie obiektu",
    labels={
        "cena_biletu_pln": "Cena biletu [PLN]",
        "wypelnienie": "Wypełnienie"
    }
)

fig.show()

print("""
Wniosek:

Nie widać silnej zależności między ceną biletu
a stopniem wypełnienia obiektu.
Droższe koncerty również osiągają wysoką frekwencję.
""")


# MAPA POLSKI


mapa = (
    df.groupby("miasto")
    .agg(
        srednia_cena=("cena_biletu_pln", "mean"),
        liczba_koncertow=("event_id", "count"),
        przychod=("przychod_pln", "sum"),
        latitude=("latitude", "first"),
        longitude=("longitude", "first")
    )
    .reset_index()
)

fig = px.scatter_mapbox(
    mapa,
    lat="latitude",
    lon="longitude",
    size="liczba_koncertow",
    color="srednia_cena",
    hover_name="miasto",
    hover_data=[
        "liczba_koncertow",
        "srednia_cena",
        "przychod"
    ],
    zoom=5.5,
    height=700,
    mapbox_style="open-street-map",
    title="Mapa koncertów w Polsce"
)

fig.show()


# DANE DO SUBPLOTÓW


miasta_przychod = (
    df.groupby("miasto")["przychod_pln"]
    .sum()
    .sort_values(ascending=False)
)

gatunki = (
    df.groupby("gatunek")
    .size()
    .sort_values(ascending=False)
)

# SUBPLOTY 2x2


fig = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=(
        "Przychód według miasta",
        "Liczba koncertów według gatunku",
        "Rozkład cen biletów",
        "Wypełnienie według typu obiektu"
    )
)


# 1. Przychody wg miasta


fig.add_trace(
    go.Bar(
        x=miasta_przychod.index,
        y=miasta_przychod.values,
        name="Przychód"
    ),
    row=1,
    col=1
)


# 2. Gatunki


fig.add_trace(
    go.Bar(
        x=gatunki.index,
        y=gatunki.values,
        name="Koncerty"
    ),
    row=1,
    col=2
)


# 3. Histogram


fig.add_trace(
    go.Histogram(
        x=df["cena_biletu_pln"],
        nbinsx=40,
        name="Cena biletu"
    ),
    row=2,
    col=1
)


# 4. Boxplot


for typ in df["typ_obiektu"].unique():

    fig.add_trace(
        go.Box(
            y=df[df["typ_obiektu"] == typ]["wypelnienie"],
            name=typ,
            showlegend=False
        ),
        row=2,
        col=2
    )

fig.update_layout(
    title="Podsumowanie rynku koncertów w Polsce",
    height=900
)

fig.show()


# WNIOSKI


print("""

WNIOSKI


1. Warszawa generuje najwyższy łączny przychód z koncertów.

2. Największa liczba wydarzeń odbywa się w największych miastach,
   szczególnie w Warszawie, Krakowie i Wrocławiu.

3. Najwyższe przychody osiągają koncerty organizowane
   na stadionach i festiwalach.

4. Rozkład cen biletów jest zbliżony do normalnego,
   z niewielką liczbą bardzo drogich wydarzeń.

5. Nie widać silnej zależności pomiędzy ceną biletu
   a stopniem wypełnienia obiektu.
""")
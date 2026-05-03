import pydeck as pdk

def crime_map(df):

    df = df.dropna(subset=["Latitude", "Longitude"])

    df_sample = df.sample(min(len(df), 20000))

    layer = pdk.Layer(
        "ScatterplotLayer",
        data=df_sample,
        get_position="[Longitude, Latitude]",
        get_radius=60,
        get_fill_color=[255, 0, 0, 140],
        pickable=True,
    )

    view_state = pdk.ViewState(
        latitude=df["Latitude"].mean(),
        longitude=df["Longitude"].mean(),
        zoom=10,
        pitch=40,
    )

    return pdk.Deck(layers=[layer], initial_view_state=view_state)
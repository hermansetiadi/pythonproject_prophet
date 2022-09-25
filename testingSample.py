def test_01():
    import pandas as pd
    from neuralprophet import NeuralProphet, set_log_level
    set_log_level("ERROR")
    data_location = "https://raw.githubusercontent.com/ourownstory/neuralprophet-data/main/datasets/"

    df = pd.read_csv(data_location + "yosemite_temps.csv")
    df.to_csv("weather.csv")
    exit()
    m = NeuralProphet(
        n_changepoints=0,
        weekly_seasonality=False,
    )
    metrics = m.fit(df, freq='5min')
    future = m.make_future_dataframe(df, periods=7 * 288, n_historic_predictions=True)
    forecast = m.predict(future)
    fig = m.plot(forecast)
    # fig_comp = m.plot_components(forecast)
    fig_param = m.plot_parameters()
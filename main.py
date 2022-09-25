# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# jkon
from threading import Thread

import dataparserwinlose
import testingSample

NAMA_SAHAM = "ltls"


def updatenamasaham(xxx):
    global NAMA_SAHAM
    NAMA_SAHAM = xxx
    f = open('lastsaham.txt', 'wt', encoding='utf-8')
    f.write(xxx)


def getnamasaham():
    with open('lastsaham.txt') as f:
        contents = f.read()
        if contents == "":
            updatenamasaham("LTLS")
            return "LTLS"
        else:
            global NAMA_SAHAM
            NAMA_SAHAM = contents
            return NAMA_SAHAM


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

def proc(input):
    import yfinance as yf

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    data = yf.download(
        tickers=str(NAMA_SAHAM).upper() + ".JK",
        period="1y",
        interval="1d",
    )
    data.to_csv("auto.csv")
    # print(data)
    # yf.actions.to_csv("tickertag{}.csv".format(url))
    # Load the dataset using pandas
    data = pd.read_csv("auto.csv")
    print(data.head(5))
    print(data.describe())

    # data2 = pd.read_csv("data.csv")
    #
    # print(data2)

    # exit()

    # Select only the important features i.e. the date and price
    # select Date and Price
    data = data[["Date", "Close"]]

    # Rename the features: These names are NEEDED for the model fitting
    # renaming the columns of the dataset
    data = data.rename(columns={"Date": "ds", "Close": "y"})
    print(data.head(5))

    from neuralprophet import NeuralProphet

    help(NeuralProphet)

    # m = NeuralProphet() # default model
    # our model
    # input_mode =  input("masukkan mode: (1 atau 2)")

    input_mode = input

    # window.close()
    GR = 1.618
    m = NeuralProphet(
        n_forecasts=int(60 / GR),
        n_lags=int(60 / GR),
        n_changepoints=int(60 * GR),
        yearly_seasonality=False,
        weekly_seasonality=True,
        # daily_seasonality=false,
        batch_size=int(64 / GR / GR),
        epochs=int(100 * GR * GR),
        learning_rate=1,
    )

    if input_mode == "2":
        del m
        m = NeuralProphet(
            n_forecasts=3,
            n_lags=3,
            n_changepoints=2,
            yearly_seasonality=False,
            weekly_seasonality=True,
            daily_seasonality=True,
            batch_size=64,
            epochs=100,
            learning_rate=1.0,
        )

    if input_mode == "3":
        del m
        m = NeuralProphet(
        )

    # m.add_country_holidays(country_name='ID')

    # fit the model using all data
    metrics = m.fit(data, freq="D")
    # with cross-validation
    # metrics = m.fit(data,
    #                 freq="D",
    #                 valid_p=0.2, # validation proportion of data (20%)
    #                 epochs=100)

    # Predictions
    # we need to specify the number of days in future

    future = m.make_future_dataframe(data, periods=45, n_historic_predictions=len(data))
    prediction = m.predict(future)
    # Plotting
    forecast = m.plot(prediction)
    # forecast = m.plot_components(prediction)
    forecast = m.plot_parameters()

    plt.title("Prediction Stock Price for the next 60 days: " + NAMA_SAHAM.upper())
    plt.xlabel("Date")
    plt.ylabel("Close Stock Price")
    plt.tight_layout()
    plt.show()


def screen():
    input_mode = 0
    import PySimpleGUI as sg

    layout = [[sg.Text(getnamasaham().upper())]
        , [sg.Text("input saham: "), sg.InputText()]
        , [sg.Button("END")]
        , [sg.Button("CLOSE")]
        , [sg.Button("1")]
        , [sg.Button("2")]
        , [sg.Button("3")]
        , [sg.Button("TEST WEATHER")]
        , [sg.Button("DATA READER")]
              ]
    window = sg.Window("Cek Saham", layout)

    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button

        if event == sg.WIN_CLOSED:
            exit()
        if event == "END":
            exit()

        if event == "CLOSED":
            input_mode = "99"
            break
        if event == "1":
            input_mode = "1"
            if values[0] != "":
                updatenamasaham(values[0])
            break
        if event == "2":
            input_mode = "2"
            if values[0] != "":
                updatenamasaham(values[0])
            break
        if event == "3":
            input_mode = "3"
            if values[0] != "":
                updatenamasaham(values[0])
            break
        if event == "TEST WEATHER":
            testingSample.test_01()
            break;
        if event == "DATA READER":
            dataparserwinlose.showMostActive()
            dataparserwinlose.showWinner()
            dataparserwinlose.showLoser()
            dataparserwinlose.showWinner_notListed()
            dataparserwinlose.showLoser_notListed()
            exit()
            break;
    window.close()
    return input_mode


def screenError():
    import PySimpleGUI as sg2
    layout = [[sg2.Text(getnamasaham().upper() + " ERROR!")]
              ]
    window2 = sg2.Window("Info", layout)

    while True:
        event, values = window2.read()
        # End program if user closes window or
        # presses the OK button

        if event == sg2.WIN_CLOSED:
            window2.close()
            break


def screenLoading():
    import PySimpleGUI as sg
    layout = [[sg.Text(getnamasaham().upper() + " Loading ...")]
              ]
    window2 = sg.Window("Info", layout).Finalize()
    return window2


def screenLoadingClose(window):
    window.close()


if __name__ == '__main__':
    print_hi('PyCharm')
    input_mode = 0
    while input_mode != 99:
        input_mode = screen()

        try:
            window = screenLoading()
            proc(input_mode)
            screenLoadingClose(window)
        except:
            screenError()

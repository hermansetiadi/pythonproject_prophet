datamain = []


# from google.colab import drive
# drive.mount('/content/drive/Colab Notebooks/datasaham')
def showMostActive():
    print("---- MOST ACTIVE ----")

    filepath1 = 'aaa.txt'
    with open("DataToParse/" + filepath1) as fp:
        data2 = fp.readlines()
        cnt = 0
        for data1 in data2:
            if len(data1.strip()) == 4:
                location = 4 + data2.index(data1)
                datamain.append(data1.strip())
                datamain.append(data2[location].strip())
    print(datamain)


def showWinner():
    print("---- WINNER ----")
    filepath2 = '0win.txt'
    with open("DataToParse/" + filepath2) as fp:
        lines = fp.readlines()
        for line in lines:
            konten = line.strip()
            if len(konten) == 4:
                if konten in datamain:
                    location = datamain.index(konten)
                    print(datamain[location] + " " + datamain[location + 1])


def showLoser():
    print("---- LOSER ----")

    filepath3 = '0lose.txt'
    with open("DataToParse/" + filepath3) as fp:
        lines = fp.readlines()
        for line in lines:
            konten = line.strip()
            if len(konten) == 4:
                if konten in datamain:
                    location = datamain.index(konten)
                    print(datamain[location] + " " + datamain[location + 1])


def showWinner_notListed():
    print("---- WINNER but NOT LISTED ----")
    filepath2 = '0win.txt'
    with open("DataToParse/" + filepath2) as fp:
        lines = fp.readlines()
        for line in lines:
            konten = line.strip()
            if len(konten) == 4:
                if konten not in datamain:
                    location = lines.index(konten + "\n")
                    percentage = lines[location + 4]
                    percentage = percentage.strip()
                    print(konten + " " + percentage)


def showLoser_notListed():
    print("---- LOSER but NOT LISTED ----")

    filepath3 = '0lose.txt'
    with open("DataToParse/" + filepath3) as fp:
        lines = fp.readlines()
        for line in lines:
            konten = line.strip()
            if len(konten) == 4:
                if konten not in datamain:
                    location = lines.index(konten + "\n")
                    percentage = lines[location + 4]
                    percentage = percentage.strip()
                    print(konten + " " + percentage)

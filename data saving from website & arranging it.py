import requests ,pickle
file=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
with open("data.txt","w") as f:
    f.write(file.text)
with open("data.txt", "r") as f:
    filee=f.read()
    filee=filee.split("\n")
    filee=[f.split(",") for f in filee if len(f)!=0]
with open("data2.txt","wb") as f2:
    pickle.dump(filee,f2)
with open("data2.txt","rb") as f2:
    print(pickle.load(f2))
input()
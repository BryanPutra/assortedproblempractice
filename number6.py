def histogram(listint):
    for i in listint:
        starempty = ""
        times = i
        while(times > 0):
            starempty += "*"
            times = times - 1
        print(starempty)

histogram([2,5,8,9])
histogram([4,9,7])
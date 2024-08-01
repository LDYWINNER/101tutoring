import requests


def is_it_down():
    print("Welcome to IsItDown.py!")
    print("Please write a URL or URLs you want to check. (separated by comma)")

    temp = input()
    urls = temp.split(",")

    result = []
    for url in urls:

        if ".com" not in url:
            print(url.strip() + " is not a valid URL.")
            exit()

        url = url.lower().strip()

        if "http" in url:
            result.append(url)
        else:
            url = "http://" + url
            result.append(url)

    # print(result)

    for x in result:
        try:
            r = requests.get(x)
            if r.status_code == 200:
                print(x + " is up!")
        except:
            print(x + " is down!")


is_it_down()

done = input("Do you want to start over? y/n ").lower()
if done == "y":
    is_it_down()
elif done == "n":
    print("k, bye!")
    exit()
else:
    print("That's not a valid answer")
    done = input("Do you want to start over? y/n ").lower()

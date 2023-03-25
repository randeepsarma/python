import concurrent.futures
import requests


def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")


url = "https://picsum.photos/2000/3000"
if __name__ == "__main__":
    """
    pros = []
    for i in range(5):
        # synchronous execution
        # downloadFile(url, i)
        p = multiprocessing.Process(target=downloadFile, args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()"""
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for i in range(10)]
        l2 = [i for i in range(10)]
        results = executor.map(downloadFile, l1, l2)


def read_locations():
    locations = []

    with open("MOCK_DATA.csv", encoding="utf8") as f:
        i = 0
        for line in f:
            """első sor miatt ki kell szedni"""
            i +=1
            if i == 1:
                continue 
            """kitörli a plusz sort és szétvágja vesszőknél, beleteszi a parts ba"""
            parts = line.strip().split(",")
            name = parts[0]
            coord = parts[1] + "," + parts[2]
            """append beleteszi a location klistába"""
            locations.append((name,coord))
    return locations


"""ha importáljuk automítikusan lefutnak a nem fgvek is és ezért ami ez után van az más oldalon importáláskor nem fut le"""
if __name__ == "__main__":
    for name, coords in read_locations():
        print(f"{name} --- {coords}")
file = open("Scores.csv","a")
name = "aaa"
score = 127
time = 23
file.write(f"\n{name},{score},{time}")
file.close()
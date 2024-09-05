#wap in python o genreate multiplication tablen foem 2 20 in multiplication files, 
for i in range(2,21):
    with open(f"multiplication//multiplication_file_{i}.txt","w") as t:
        for j in range(1,11):
            t.write(f"{i}X{j}={i*j}")
            if j!=11:
                t.write("\n")
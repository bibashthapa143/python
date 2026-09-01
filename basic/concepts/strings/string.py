#use of F-string
name="Eros"
port=443
print(f"{name} is checking port {port}")

print("-------------------------------------------------")

#common string method.
text=" Hello World "
print(text.strip())  #removes unwanted spacing
print(text.strip().lower())
print(text.strip().upper())
print(text.strip().replace("o","0"))


print("-------------------------------------------------")
line = "80 444 8080"
ports = line.split(" ")       # ['80', '443', '8080']  -> now a list!
print(ports)

print("-------------------------------------------------")
back = " + ".join(ports)        # '80,443,8080'  -> list back to string
print(back)

print("22,80,443".split(","))
# ↑ the thing being split has the dot

print(",".join(["22", "80", "443"]))
#    ↑ the glue has the dot


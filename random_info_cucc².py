while True:
    try: x, y, z = int(input("Első szám > ")), int(input("Második szám > ")), 0
    except: continue
    if x < y:
        z,x,y = x,y,z
    break
print(f"\n{x}-ben a {y} megvan {round(x/y)}-szor, a maradék pedig {x%y}\nMert {y} X {round(x/y)} = {y*round(x/y)} + {x%y} = {x}")
input()
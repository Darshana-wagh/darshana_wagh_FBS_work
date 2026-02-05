
area_one_wall = float(input("Enter area of one wall: "))
interior_cost = float(input("Enter cost per unit area (interior): "))
exterior_cost = float(input("Enter cost per unit area (exterior): "))

interior_walls = 2
exterior_walls = 6

interior_paint_cost = interior_walls * area_one_wall * interior_cost
exterior_paint_cost = exterior_walls * area_one_wall * exterior_cost

total_cost = interior_paint_cost + exterior_paint_cost

print("Interior painting cost:", interior_paint_cost)
print("Exterior painting cost:", exterior_paint_cost)
print("Total painting cost:", total_cost)


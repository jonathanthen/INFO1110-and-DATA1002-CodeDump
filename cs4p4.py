def calculate_cat_food_required(breed, weight_in_kilograms):
    weight = float(weight_in_kilograms)
    
    if breed == "bengal":
        cups = 0.2 * weight
        
    elif breed == "scottish_fold":
        cups = 0.4 * weight
        
    elif breed == "fat_cat":
        cups = 0.5 * weight
        
    else:
        cups = 0.3 * weight
    
    return cups

litter = 3 * (calculate_cat_food_required("scottish_fold", 0.9))
print(litter)
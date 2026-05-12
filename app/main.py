def get_human_age(cat_age: int, dog_age: int) -> list:
    """
    Convert cat and dog ages to human years.
    
    Rules:
    Cat: first 15 years = 1 human year, next 9 = +1, then every 4 = +1
    Dog: first 15 years = 1 human year, next 9 = +1, then every 5 = +1
    
    Args:
        cat_age: Cat's age in cat years
        dog_age: Dog's age in dog years
        
    Returns:
        List with [cat_human_age, dog_human_age]
        
    Examples:
        get_human_age(0, 0) == [0, 0]
        get_human_age(15, 15) == [1, 1]
        get_human_age(24, 24) == [2, 2]
    """
    def calculate_years(age: int, extra_step: int) -> int:
        # Менше 15 років — 0 людських років
        if age < 15:
            return 0
        
        # Від 15 до 23 років — 1 людський рік
        if age < 24:
            return 1
        
        # 24 роки і більше: 
        # 2 (за перші 24 роки) + залишок, поділений на крок (4 для котів, 5 для собак)
        return 2 + (age - 24) // extra_step

    return [
        calculate_years(cat_age, 4),
        calculate_years(dog_age, 5)
    ]

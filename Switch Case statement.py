from typing import List
import math
def areaSwitchCase(ch: int, a: List[float]) -> str:
    if ch == 1:
        r = a[0] 
        area = math.pi * r * r 
        return f"{area:.5f}"  
    elif ch == 2:
        l = a[0]  
        b = a[1]  
        area = l * b  
        return f"{area:.5f}"  
    else:
        return "Invalid choice"

def hammingDistance(p: str, q: str) -> int:
    
    i = 0
    
    while i < len(q):
        if p[i] == q[i]:
                count+=1
        i+=1
        
    return count

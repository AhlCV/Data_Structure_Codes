import sys

def towers(n : int, src : int, dest : int) -> None:
    if n == 1: # Base case: If there's only one disk, move it directly via moveDisk.
        moveDisk(src, dest) # Move the largest disk directly from src to dest.
    else:
        tmp = 6 - src - dest
        towers(n - 1, src, tmp)#Recursively move n-1 disks from the src to the tmp peg (using dest as 
        #temporary).
        moveDisk(src, dest)
        towers(n - 1, tmp, dest)#Recursively move n-1 disks from the tmp peg to the dest peg 
        #(using src as temporary).
        

def moveDisk(src : int, dest : int) -> None:
    print(f"Moving top disk from peg {src} to peg {dest}")

if __name__ == "__main__":
    try:
        towers(*[int(x) for x in sys.argv[1:]])#Gets the arguments, converts them to integers, and then 
        #'un-packs' them as separate parameters when calling the towers function.
    except:
        print("Usage: python3 Hanoi.py <n> <src> <dest>")#Initial Call

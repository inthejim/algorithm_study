def largest_rectangle_area(heights):
    stack = []
    max_area = 0

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            print("i",i)
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            print("height:",height, "width",width)
            max_area = max(max_area, height * width)

        stack.append(i)

    while stack:
        height = heights[stack.pop()]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area

def main():
    while True:
        n, *heights = map(int, input().split())
        if n == 0:
            break

        result = largest_rectangle_area(heights)
        print(result)

if __name__ == "__main__":
    main()

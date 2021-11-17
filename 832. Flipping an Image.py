class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        iv = []
        r = []
        for i in range(0,len(image)):
            image[i] = image[i][::-1]
        for i in image:
            for j in range(0,len(i)):
                i[j] = 1 - i[j]
        return image
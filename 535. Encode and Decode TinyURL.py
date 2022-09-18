class Codec:
    def __init__(self):
        self.hash = []
        self.counter = -1

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.hash.append(longUrl)
        self.counter += 1
        return f"{self.counter}"
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hash[int(shortUrl)]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
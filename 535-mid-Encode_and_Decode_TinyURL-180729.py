"""
535. Encode and Decode TinyURL

Note: This is a companion problem to the System Design problem: Design TinyURL.
https://leetcode.com/discuss/interview-question/system-design/
https://leetcode.com/discuss/interview-question/124658/Design-a-URL-Shortener-(-TinyURL-)-System/
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

"""

# Result AC 100 % 24ms

# class Codec:

#     def encode(self, longUrl):
#         return longUrl

#     def decode(self, shortUrl):
#         return shortUrl


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


# Result 28ms 82.46%

class Codec:
    import string
    letters = string.ascii_letters + string.digits
    full_tiny = {}
    tiny_full = {}
    global_counter = 0
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        def decto62(dec):
            ans = ""
            while 1:
                ans = self.letters[dec % 62] + ans
                dec //= 62
                if not dec:
                    break
            return ans
                
        suffix = decto62(self.global_counter)
        if longUrl not in self.full_tiny:
            self.full_tiny[longUrl] = suffix
            self.tiny_full[suffix] = longUrl
            self.global_counter += 1
        return "http://tinyurl.com/" + suffix
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        idx = shortUrl.split('/')[-1]
        if idx in self.tiny_full:
            return self.tiny_full[idx]
        else:
            return None


if __name__ == '__main__':
    from time import time
    codec = Codec()
    t = time()
    ans = codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl"))
    print('ans: %s\ntime: %.3fms' % (ans, (time() - t) * 1000))             
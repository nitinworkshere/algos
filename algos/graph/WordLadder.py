import collections


def ladderLength(beginWord, endWord, wordList):
    dic = set(wordList)
    if endWord not in dic:
        return 0
    q = collections.deque()
    q.append(beginWord)
    count = 1
    while q:
        size = len(q)
        count += 1
        for _ in range(size):
            w = q.popleft()
            for i in range(len(w)):
                for c in range(ord('a'), ord('z') + 1):
                    nw = w[:i] + chr(c) + w[i + 1:]
                    if nw == endWord:
                        return count
                    if nw in dic:
                        q.append(nw)
                        dic.remove(nw)
    return 0


print(ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"] ))

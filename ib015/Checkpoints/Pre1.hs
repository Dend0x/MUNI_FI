jeJineNezNula :: Integer -> Bool
jeJineNezNula 0 = True
jeJineNezNula _ = False

jeDelitelny :: Integer -> Integer -> Bool
jeDelitelny a b = jeJineNezNula(a - b * ((div) a b))

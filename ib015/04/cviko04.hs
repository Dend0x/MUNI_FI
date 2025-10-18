oddify :: Integral a => [a] -> [a]
oddify xs = map (\x -> if even x then x + 1 else x) xs

inputWithOddified :: Integral a => [a] -> [(a, a)]
inputWithOddified xs = zip xs (oddify xs)
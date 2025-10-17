returnNPairs :: Int -> [(Integer, Integer)]
returnNPairs n = take n [(i, n - i + 1) | n <- [1, 2..], i <- [1..n]]
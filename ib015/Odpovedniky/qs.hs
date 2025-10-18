qsort :: Ord a => [a] -> [a]
qsort [] = []
qsort (p:s) = qsort [ x | x <- s, x < p] ++ [p] ++ qsort [x | x <- s, x >= p]
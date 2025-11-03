evalPoly :: Num a => [a] -> a -> a
evalPoly coeffs x = foldr (\a b -> b * x + a) 0 coeffs

f :: (Num a, Ord a) => [a] -> [a] -> [a]
f [] _ = []
f _ [] = []
f (x:xs) (y:ys) = if x > y
    then ((^) (y * 42) 2) : f xs ys
    else f xs ys

repeatUntil :: (a -> a) -> (a -> a -> Bool) -> a -> a

repeatUntil f p start = if p start (f start) then f start else repeatUntil f p (f start)
import Data.List (groupBy, sortOn, nub)

evalPoly :: Num a => [a] -> a -> a
evalPoly coeffs x = foldr (\a b -> b * x + a) 0 coeffs

f :: (Num a, Ord a) => [a] -> [a] -> [a]
f [] _ = []
f _ [] = []
f (x:xs) (y:ys) = if x > y
    then ((^) (y * 42) 2) : f xs ys
    else f xs ys

repeatUntil :: (a -> a) -> (a -> a -> Bool) -> a -> a
<<<<<<< HEAD
repeatUntil f p start = if p start (f start) then f start else repeatUntil f p (f start)

books :: [(String, String, Int)]
books = [
  ("The Lord of the Rings", "The Fellowship of the Ring", 1954),
  ("The Lord of the Rings", "The Two Towers", 1954),
  ("The Lord of the Rings", "The Return of the King", 1955),
  ("Harry Potter", "Philosopher's Stone", 1997),
  ("Harry Potter", "Chamber of Secrets", 1998),
  ("Harry Potter", "Prisoner of Azkaban", 1999),
  ("Harry Potter", "Goblet of Fire", 2000),
  ("Harry Potter", "Order of the Phoenix", 2003),
  ("Harry Potter", "Half-Blood Prince", 2005),
  ("Harry Potter", "Deathly Hallows", 2007),
  ("Mistborn: Era One", "The Final Empire", 2006),
  ("Mistborn: Era One", "The Well of Ascension", 2007),
  ("Mistborn: Era One", "The Hero of Ages", 2008),
  ("Hyperion Cantos", "Hyperion", 1989),
  ("Hyperion Cantos", "The Fall of Hyperion", 1990),
  ("Hyperion Cantos", "Endymion", 1996),
  ("Hyperion Cantos", "The Rise of Endymion", 1997),
  ("The Kingkiller Chronicle", "The Name of the Wind", 2007),
  ("The Kingkiller Chronicle", "The Wise Man's Fear", 2011)]


selectSuitableSeries :: [(String, String, Int)] -> [String]
selectSuitableSeries xs = nub (map (fstThree . head) (filter (\x -> length x <= 4 && all ((<=2010) . thdThree) x) (groupBy (\x y -> fstThree x == fstThree y) (sortOn fstThree xs))))
                        where fstThree (x, _, _) = x
                              thdThree (_, _, x) = x
=======
repeatUntil f p start = if p start (f start) then f start else repeatUntil f p (f start)
>>>>>>> 5f0a1e2da693f269ed28149bc2eb41365dca9b76

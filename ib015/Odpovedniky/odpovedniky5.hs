ascendingBySteps :: Integer -> Integer -> [Integer]
ascendingBySteps m n = [ y | x <- [1..m], y <- [1, 1+x..n]]

group :: Eq a => [a] -> [[a]]
group = foldr (\x y -> if y == [] then [[x]] else if x == (head.head) y then (x : head y) : tail y else [x] : y) []

pascal :: [[Integer]]
pascal = iterate (\x -> zipWith (+) (0 : x) (x ++ [0])) [1]

list :: [Integer]
list = [10^10^10, 1, 2, let inf = inf in inf, 4, 5]

data Deed = GoodDeed Integer | BadDeed Integer deriving (Show, Eq)

data Present = Present String Integer deriving (Show, Eq)
type Wishlist = [Present]

wasGood :: Deed -> Integer -> Integer
wasGood (GoodDeed x) y = y + x
wasGood (BadDeed x) y = y - x 

whatforthem :: Integer -> Wishlist -> [String]
whatforthem _ [] = []
whatforthem n ((Present nazev cena):xs) = if n >= cena then nazev : whatforthem (n - cena) xs else whatforthem n xs

assignPresents :: [([Deed], Wishlist)] -> [[String]]
assignPresents xs = map present xs
    where present xs = whatforthem (foldr wasGood 0 (fst xs)) (snd xs)

babyJesusData =
  [
    ([GoodDeed 10, BadDeed 3, GoodDeed 2],
     [Present "kolo" 5, Present "pes" 5, Present "ponozky" 2]),
    ([GoodDeed 10, BadDeed 3],
     [Present "nove brnenske nadrazi" 100, Present "A z IB015" 5, Present "iPhone" 5]),
    ([GoodDeed 10, BadDeed 3, BadDeed 100],
     [Present "ponozky" 2]),
    ([BadDeed 10, GoodDeed 20],
     [Present "you" 10])
  ]
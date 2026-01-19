reversePrefix :: [Int] -> [Int]
reversePrefix [] = []
reversePrefix (x:xs) = if length xs >= 5 then reverse (take x xs) ++ drop x xs else x:xs

help' :: Int -> [Int] -> [Int]
help' 0 _ = []
help' n (x:xs) = help' (n - 1) xs ++ [x]

reversePrefix' :: [Int] -> [Int]
reversePrefix' [] = []
reversePrefix' (x:xs) = if length xs >= 5 then help' x (take x xs) ++ drop x xs else x:xs

printSum :: [Int] -> IO()
printSum xs = putStrLn (show (sum xs))

data Tree a b = Leaf a | Node b (Tree a b) (Tree a b)

treeFold::(a -> c) -> (b -> c -> c -> c) -> Tree a b ->c
treeFold lf nf (Leaf a) = lf a
treeFold lf nf (Node b t1 t2) = nf b (treeFold lf nf t1) (treeFold lf nf t2)

prodLeaves :: Tree Int b -> Int
prodLeaves tr = treeFold id (\_ y z -> y * z) tr

suffixSums :: [Int] -> [Int]
suffixSums xs = map (\x -> sum(drop x xs)) [0..length xs - 1]

suffixSums' :: [Int] -> [Int]
suffixSums' [] = []
suffixSums' (x:xs) = sum (x:xs) : suffixSums' xs

greetUser :: IO()
greetUser = putStr "Jméno: " >> getLine >>= putStr >> putStr ", Věk: " >> getLine >>= putStrLn

dva :: IO ()
dva = getLine >>= \c1 -> getLine >>= \c2 -> putStrLn(show ((read c1 :: Integer) + (read c2 :: Integer)))

bin :: [Bool] -> Int
bin = foldl (\x y -> if y then 2 * x + 1 else 2 * x) 0
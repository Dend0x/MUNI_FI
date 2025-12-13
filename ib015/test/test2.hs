gen :: [(Integer, Integer, Integer)]
gen = [ (x, y, (x - y)) | x <- [0,1..], y <- [0..x]]

data FemaleTree = FemOutHus String | FemWitHus String String [FemaleTree]
    deriving Show

mops = FemWitHus "sex" "bob" [(FemOutHus "mo"), (FemWitHus "bob" "sex" [(FemOutHus "bobina"), (FemOutHus "mopa")])]

arabs :: FemaleTree -> Integer
arabs (FemOutHus "Arabela") = 1
arabs (FemOutHus _) = 0
arabs (FemWitHus _ _ xs) = if s == 0 then 0 else s + 1
    where s = foldr (\x y -> max x y) 0 (map arabs xs)


otoc :: [a] -> [a]
otoc = foldr (\x y -> y ++ [x]) []
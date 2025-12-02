import Data.Char (isUpper)

nth :: [a] -> Int -> a
nth n = (head . (flip drop n))

firstUppercase :: String -> Char
firstUppercase str = if length xs == 0 then '-' else head xs
                where xs = dropWhile (not . isUpper) str

everyNth :: [a] -> Int -> [a]
everyNth xs n = map snd (filter ((==0) . (flip mod n) . fst) (zip [0..] xs))

binmap :: (a -> a -> b) -> [a] -> [b]
binmap _ [] = []
binmap f (x:xs) = map (\x -> f (fst x) (snd x)) (zip (x:xs) xs)

data BinLeafTree a = LLeaf a | LNode (BinLeafTree a) (BinLeafTree a)
    deriving (Show, Eq)

ltSumEven :: Integral a => BinLeafTree a -> a
ltSumEven (LLeaf x) = if even x then x else 0
ltSumEven (LNode l r) = ltSumEven l + ltSumEven r

data RoseLeafTree a = RLNode [RoseLeafTree a] | RLLeaf a
    deriving (Show, Eq)

countValueLeaves :: RoseLeafTree a -> Integer
countValueLeaves (RLLeaf _) = 1
countValueLeaves (RLNode xs) = (sum . map countValueLeaves) xs
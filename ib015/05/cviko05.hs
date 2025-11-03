import Data.Maybe (isJust, fromJust)

-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * --
type WeaponsPoints = Integer
type HealthPoints = Integer

data Armor = Leather | Steel -- kožené nebo ocelové brnění
             deriving (Eq, Show)

data Warrior = Warrior HealthPoints Armor WeaponsPoints
               deriving (Eq, Show)

attack :: Warrior -> Warrior -> Warrior
attack (Warrior _ _ w) (Warrior h2 a2 w2) = if a2 == Steel then (Warrior (h2 - (div w 2)) a2 w2) else (Warrior (h2 - w) a2 w2)

warrior1 = Warrior 30 Leather 30
warrior2 = Warrior 20 Steel 25

-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * --

data Jar = EmptyJar | Jam String | Cucumbers | Compote Int

today = 2025

stale :: Jar -> Bool
stale (Compote x) = today > x + 10

-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * --

divlist :: Integral a => [a] -> [a] -> [Maybe a]
divlist = zipWith (\x y -> if y == 0 then Nothing else Just (div x y))

-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * --

addVars :: String -> String -> [(String, Integer)] -> Maybe Integer
addVars a b xs = if isJust (lookup a xs) && isJust (lookup b xs) then Just (fromJust (lookup a xs) + fromJust (lookup b xs)) else Nothing

-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * --

mayZip :: [a] -> [b] -> [(Maybe a, Maybe b)]
mayZip [] [] = []
mayZip [] (x:xs) = (Nothing, Nothing) : mayZip [] xs
mayZip (x:xs) [] = (Nothing, Nothing) : mayZip xs []
mayZip (x:xs) (y:ys) = (Just x,Just y) : mayZip xs ys 

-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * --

data Mark = A | B | C | D | E | F | X | S deriving (Eq, Show)
type StudentName = String
type CourseName = String
data StudentResult = StudentResult StudentName CourseName (Maybe Mark)
                     deriving (Eq, Show)

-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * --
data Nat = Zero | Succ Nat deriving Show

natToInt :: Nat -> Int
natToInt = undefined

-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * --
data Expr = Con Double
          | Add Expr Expr | Sub Expr Expr
          | Mul Expr Expr | Div Expr Expr
          deriving Show

eval :: Expr -> Double
eval (Con a) = a
eval (Add a b) = (eval a) + (eval b)
eval (Sub a b) = (eval a) - (eval b)
eval (Mul a b) = (eval a) * (eval b)
eval (Div a b) = if isJust (evalMay (Div a b)) then fromJust (evalMay (Div a b)) else 0

evalMay :: Expr -> Maybe Double
evalMay (Div a b) = if (eval b) == 0 then Nothing else Just ((eval a) / (eval b))

-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * --
data BinTree a = Empty 
               | Node a (BinTree a) (BinTree a) 
                 deriving (Eq, Show)

tree00 :: BinTree Int
tree00 = Node 42 (Node 28 Empty Empty) Empty

tree01 :: BinTree Int
tree01 = Node 4 (Node 2 (Node 1 Empty Empty) (Node 3 Empty Empty))
                (Node 6 (Node 5 Empty Empty) (Node 7 Empty Empty))

tree02 :: BinTree Int
tree02 = Node 9 Empty (Node 11 (Node 10 Empty Empty)
                               (Node 12 Empty Empty))

tree03 :: BinTree Int
tree03 = Node 8 tree01 tree02

tree04 :: BinTree Int
tree04 = Node 4 (Node 2 Empty (Node 3 Empty Empty))
                (Node 6 (Node 5 Empty Empty) Empty)

tree05 :: BinTree Int
tree05 = Node 100 (Node 101 Empty
                            (Node 102 (Node 103 Empty
                                                (Node 104 Empty Empty))
                                      Empty))
                  (Node 99 (Node 98 Empty Empty)
                           (Node 98 Empty Empty))

emptyTree :: BinTree Int
emptyTree = Empty

-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * --
treeSize :: BinTree a -> Int
treeSize Empty = 0
treeSize (Node _ l r) = 1 + treeSize l + treeSize r 

listTree :: BinTree a -> [a]
listTree Empty = []
listTree (Node v l r) = listTree l ++ [v] ++ listTree r

height :: BinTree a -> Int
height Empty = 0
height (Node v l r) = 1 + max (height l) (height r)

longer :: [a] -> [a] -> [a]
longer x y = if length x > length y then x else y

longestPath :: BinTree a -> [a]
longestPath Empty = []
longestPath (Node v l r) = if (length (longestPath l)) > (length (longestPath r)) then [v] ++ longestPath l else [v] ++ longestPath r

-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * --
fullTree :: Int -> a -> BinTree a
fullTree = undefined

treeZip :: BinTree a -> BinTree b -> BinTree (a, b)
treeZip = undefined

-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * --
treeMayZip :: BinTree a -> BinTree b -> BinTree (Maybe a, Maybe b)
treeMayZip = undefined

-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * --
isTreeBST :: (Ord a) => BinTree a -> Bool
isTreeBST = undefined

searchBST :: (Ord a) => a -> BinTree a -> Bool
searchBST = undefined

-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * --
data RoseTree a = RoseNode a [RoseTree a]
                  deriving (Show, Read)

roseTreeSize :: RoseTree a -> Int
roseTreeSize = undefined

roseTreeSum :: Num a => RoseTree a -> a
roseTreeSum = undefined

roseTreeMap :: (a -> b) -> RoseTree a -> RoseTree b
roseTreeMap = undefined

-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * --
data LogicExpr = Pos | Neg
               | And LogicExpr LogicExpr
               | Or LogicExpr LogicExpr
               | Implies LogicExpr LogicExpr
               | Equiv LogicExpr LogicExpr

evalExpr :: LogicExpr -> Bool
evalExpr = undefined

-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * --
data IntSet = SetNode Bool IntSet IntSet -- Node isEnd zero one
            | SetLeaf
              deriving Show

insert :: IntSet -> Int -> IntSet
insert = undefined

find :: IntSet -> Int -> Bool
find = undefined

listSet :: IntSet -> [Int]
listSet = undefined

-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * --



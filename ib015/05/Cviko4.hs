import Data.Maybe (fromJust, isJust)

data Day = Mon | Tue | Wed | Thu | Fri | Sat | Sun
    deriving (Show, Eq, Ord)

weekend :: Day -> Bool
weekend Sat = True
weekend Sun = True
weekend _ = False

data Object = Cube Double Double Double -- a, b, c
            | Cylinder Double Double -- r, v

volume :: Object -> Double
volume (Cube a b c) = a * b * c
volume (Cylinder r v) = pi * (r ^ 2) * v

surface :: Object -> Double
surface (Cube a b c) = 2 * (a * b + a * c + b * c)
surface (Cylinder r v) = 2 * pi * (r ^ 2) + v * 2 * pi * r

data Contained a = NoValue | Single a | Pair a a
data Compare a = SameContainer
                | SameValue (Contained a)
                | DifferentContainer

cmpContained :: Eq a => Contained a
                    -> Maybe (Contained a)
                    -> Compare a
cmpContained NoValue (Just NoValue) =
    SameValue NoValue
cmpContained (Single x1) (Just (Single x2)) =
    if x1 == x2
        then SameValue (Single x1)
        else SameContainer
cmpContained (Pair x1 y1) (Just (Pair x2 y2)) =
    if x1 == x2 && y1 == y2
        then SameValue (Pair x1 y1)
        else SameContainer
cmpContained _ _ = DifferentContainer

safeDiv :: Integral a => a -> a -> Maybe a
safeDiv a b = if b == 0 then Nothing else Just (div a b)

valOrDef :: Maybe a -> a -> a
valOrDef Nothing x = x
valOrDef (Just a) _ = a

type WeaponsPoints = Integer
type HealthPoints = Integer

data Armor = Leather | Steel -- kožené nebo ocelové brnění
    deriving (Eq, Show)

data Warrior = Warrior HealthPoints Armor WeaponsPoints
    deriving (Eq, Show)

-- Příklad hodnot Armor a Warrior - Leather, Steel
-- Kolik hodnotových konstruktorů - Warrior, Steel, Leather
-- Kolik typových kosntruktorů - Armor a Warrior

warrior1 = Warrior 30 Leather 30
warrior2 = Warrior 20 Steel 25

attack :: Warrior -> Warrior -> Warrior
attack (Warrior h a w) (Warrior h2 a2 w2) = if a2 == Steel then (Warrior (max (h2 - (div w 2)) 0) a2 w2) else (Warrior (max (h2 - w) 0) a2 w2)

data Jar = EmptyJar | Jam String | Cucumbers | Compote Int

today = 2025

stale :: Jar -> Bool
stale (Compote x) = x + 10 < today
stale _ = False

-- data X = Value Int - Typové konstruktory = X, nulární, Hodnotové konstruktory = Value, unární
-- data M = A | B | N M - Typové konstruktory = M, nulární, Hodnotové konstruktoy = A, B, N, N je unární, jinak nulární
-- data N = C | D | M N - Typové konstruktory = N, nulární, Hodnotové kosntruktoy =  C, D, M, M je urnární, jinak nulární
-- data Ha = Hah Int Float [Hah] - Špatný zápis, Hah jako hodnotový konstruktor zapsán jako typový konstruktor
-- data FMN = T (Int, Int) (Int -> Int) [Int] - typové konstruktory = FMN, nulární, Hodnotové konstruktory = T, ternární
-- type Fat = Float -> Float -> Float - Typový alias
-- data E = E (E, E) - typové konstruktory E, nulární, Hodnotové konstruktory = E, unární

-- data N x = NVal (x -> x) - Ok
-- type Makro = a -> a - chybí typová proměnná a
-- data M = N (x, x) | N Bool | O M - Nelze použít hodnotový konstruktor vícekrát
-- type Fun a = a -> (a, Bool) -> c - chybí typová proměnná c
-- type Fun (a, c) (a, b) = (b, c) - chybný zápis typových proměnných
-- data F = X Int | Y Float | Z X - Použití hodnotového konstruktoru jako typového
-- data F = intfun Int - Nemá velké písmeno
-- data F = Makro Int -> Int - Není v zárvorkách?
-- type Val = Int | Bool - nelze dát nebo do typů
-- data X = X X X Ok

type Frac = (Int, Int)

sameFrac :: Frac -> Frac -> Bool
sameFrac (a,b) (c,d) = baseFrac (a,b) == baseFrac (c,d)

nonNegFrac :: Frac -> Bool
nonNegFrac (a,b) = a * b >= 0

plusFrac :: Frac -> Frac -> Frac
plusFrac (a,b) (c,d) = baseFrac (a * d + b * c, b * d)

minusFrac :: Frac -> Frac -> Frac
minusFrac (a,b) (c,d) = baseFrac (a * d - b * c, b * d)

multFrac :: Frac -> Frac -> Frac
multFrac (a,b) (c,d) = baseFrac (a * c, b * d)

divFrac :: Frac -> Frac -> Frac
divFrac (a,b) (c,d) = if c == 0 then (0,0) else multFrac (a,b) (d, c)

baseFrac :: Frac -> Frac
baseFrac (a,b) = ((div a (gcd a b)), (div b (gcd a b)))



commonPricing :: Int -> Float
commonPricing x = 13 * fromIntegral (x - (div x 10))

employeeDiscount :: Float -> Float
employeeDiscount = (0.85*)

studentPricing :: Int -> Float
studentPricing = fromIntegral

--data PricingType = Common | Employee | Student

--computePrice :: PricingType -> Int -> (Int -> Float) -> (Float -> Float) -> (Int -> Float) -> Float
--computePrice Common x commonPricing _ _ = commonPricing x
--computePrice Employee x commonPricing employeeDiscount _ = (employeeDiscount . commonPricing) x
--computePrice Student x _ _ studentPricing = studentPricing x

data PricingType = Common | Special (Int -> Float) | Discount (Float -> Float)

common = Common
employee = Discount employeeDiscount
student = Special studentPricing

computePrice :: PricingType -> Int -> (Int -> Float) -> Float
computePrice Common x f = f x
computePrice (Special dis) x _ = dis x
computePrice (Discount dis) x f = (dis . f) x

-- Maybe (Just 2) - KO - Maybe čeká typ, Just 2 je hodnota
-- Just Just 2 - KO - Just se naváže na jeden parametr tedy (Just Just) 2
-- Just (Just 2) - OK - Hodnota typu Num a => Maybe (Maybe a)
-- Maybe Nothing - KO - Maybe čeká typ, Nothing je hodnota
-- Nothing 3 - KO - Nothing je hodnota, nepříjímá hodnoty
-- Just [Just 3] - OK - typ Num a => Maybe [Maybe a]
-- Just - OK - funkce a -> Maybe a

-- Maybe a - OK - Just hodnota a
-- Just a - KO - a je typ, ne hodnota
-- Just (\x -> x ^ 2) - KO - Just příjímá hodnoty / OK - Korektní hotnota typu (Num a) => Maybe (a -> a)
-- Just Just -- OK - Funkce a -> Maybe a / ne funkce - Maybe (a -> Maybe a)
-- Just Just Just - OK stejné / KO - ne funkce, (Just Just) Just, nelze pak aplikovat na hodnotu

divlist :: Integral a => [a] -> [a] -> [Maybe a]
divlist = zipWith (\x y -> if y == 0 then Nothing else Just (div x y))

addVars :: String -> String -> [(String, Integer)] -> Maybe Integer
addVars x y xs = if isJust (lookup x xs) && isJust (lookup y xs)
                 then Just (fromJust (lookup x xs) + fromJust (lookup y xs))
                 else Nothing

mayZip :: [a] -> [b] -> [(Maybe a, Maybe b)]
mayZip [] [] = []
mayZip [] (x:xs) = [(Nothing, Just x)] ++ mayZip [] xs
mayZip (x:xs) [] = [(Just x, Nothing)] ++ mayZip xs []
mayZip (x:xs) (y:ys) = [(Just x, Just y)] ++ mayZip xs ys

data Mark = A | B | C | D | E | F | X | S deriving (Eq, Show)
type StudentName = String
type CourseName = String
data StudentResult = StudentResult StudentName CourseName (Maybe Mark)
    deriving (Eq, Show)

summarize :: StudentResult -> String
summarize (StudentResult name course (Just mark)) = name ++ " has " ++ show mark ++ " from " ++ course
summarize (StudentResult name course Nothing) = name ++ " has no result from " ++ course

data Nat = Zero | Succ Nat
    deriving Show
-- hodnoty typu Nat - Zero, Succ Zero, a tak dále
-- význam deriving show - bere vlasnosti z třídy Show, takže je zobrazitelná

natToInt :: Nat -> Int
natToInt Zero = 0
natToInt (Succ x) = 1 + natToInt x

data Expr = Con Double
          | Add Expr Expr | Sub Expr Expr
          | Mul Expr Expr | Div Expr Expr
          | Var

-- představuje pi - (Con 3.14)

eval :: Expr -> Double
eval (Con x) = x
eval (Add ex ey) = eval ex + eval ey
eval (Sub ex ey) = eval ex - eval ey
eval (Mul ex ey) = eval ex * eval ey
eval (Div ex ey) = eval ex / eval ey

evalMay :: Expr -> Maybe Double
evalMay (Con x) = Just x
evalMay (Add ex ey) = if isJust le && isJust re
                        then Just (fromJust le + fromJust re)
                        else Nothing
    where
        le = evalMay ex
        re = evalMay ey
evalMay (Sub ex ey) = if isJust le && isJust re
                        then Just (fromJust le - fromJust re)
                        else Nothing
    where
        le = evalMay ex
        re = evalMay ey
evalMay (Mul ex ey) = if isJust le && isJust re
                        then Just (fromJust le * fromJust re)
                        else Nothing
    where
        le = evalMay ex
        re = evalMay ey
evalMay (Div ex ey) = if isJust le && isJust re && fromJust re /= 0
                        then Just (fromJust le / fromJust re)
                        else Nothing
    where
        le = evalMay ex
        re = evalMay ey

--evalVar :: Double -> Expr -> Double
--evalVar _ (Con x) = x
--evalVar v Var = v
--evalVar v (Add ex ey) = eval v ex + eval v ey
--evalVar v (Sub ex ey) = eval v ex - eval v ey
--evalVar v (Mul ex ey) = eval v ex * eval v ey
--evalVar v (Div ex ey) = eval v ex / eval v ey

data BinTree a = Empty | Node a (BinTree a) (BinTree a)
    deriving Show


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

-- vsechny tříuzlové Node v (Node v (Node v Empty Empty) Empty) Empty
-- Node v (Node v Empty (Node v Empty Empty)) Empty
-- Node v Empty (Node v (Node v Empty Empty) Empty)
-- Node v Empty (Node v Empty (Node v Empty Empty))
-- Node v (Node v Empty Empty) (Node v Empty Empty)
-- Moc

treeSize :: BinTree a -> Int
treeSize Empty = 0
treeSize (Node _ l r) = 1 + treeSize l + treeSize r

listTree :: BinTree a -> [a]
listTree Empty = []
listTree (Node v l r) = v : listTree l ++ listTree r

height :: BinTree a -> Int
height Empty = 0
height (Node v l r) = 1 + max (height l) (height r)

longestPath :: BinTree a -> [a]
longestPath Empty = []
longestPath (Node v l r) = if length lt > length rt then v : lt else v : rt
    where lt = longestPath l
          rt = longestPath r

fullTree :: Int -> a -> BinTree a
fullTree 0 _ = Empty
fullTree n v = Node v (fullTree (n - 1) v) (fullTree (n - 1) v)

treeZip :: BinTree a -> BinTree b -> BinTree (a, b)
treeZip (Node v l r) (Node v2 l2 r2) = (Node (v, v2) (treeZip l l2) (treeZip r r2))
treeZip _ _ = Empty

treeMayZip :: BinTree a -> BinTree b -> BinTree (Maybe a, Maybe b)
treeMayZip Empty Empty = Empty
treeMayZip Empty (Node v l r) = (Node (Nothing, Just v) (treeMayZip Empty l) (treeMayZip Empty r))
treeMayZip (Node v l r) Empty = (Node (Just v, Nothing) (treeMayZip l Empty) (treeMayZip r Empty))
treeMayZip (Node v l r) (Node v2 l2 r2) = (Node (Just v, Just v2) (treeMayZip l l2) (treeMayZip r r2))

isOk :: (Ord a) => Bintree a -> a -> Integer -> Bool
isOk Empty _ _ = True
isOk (Node v2 _ _) v 0 = v >= v2
isOk (Node v2 _ _) v 1 = v <= v2

isTreeBST :: (Ord a) => BinTree a -> Bool
isTreeBST Empty = True
isTreeBST (Node v l r) = if 
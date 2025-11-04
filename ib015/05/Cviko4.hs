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
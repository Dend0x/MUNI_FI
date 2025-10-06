task1 :: Integral a => [a] -> a -> a -> [a]
task1 x a b = filter (divisible b) (map (* a) x)
    where divisible b x = mod x b == 0

task2 :: [String] -> Int -> Int -> Bool
task2 x a b = length x >= a && and (map (>= b) (map length x))

inner :: Integer -> [Integer]
inner 1024 = [1024]
inner x = [x..2*x - 1] ++ (inner (2 * x))


task3 :: [Integer]
task3 = inner 1
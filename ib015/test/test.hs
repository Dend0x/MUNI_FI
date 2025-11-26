fn :: [Int] -> [Int]
fn [] = []
fn (_:xs) = sum xs : fn xs

fn' :: [Int] -> [Int]
fn' xs = [ sum (drop x xs) | x <- [1..length xs]]
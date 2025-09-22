isRightTriangle :: Double -> Double -> Double -> Bool
isRightTriangle a b c = isCorrect a b c || isCorrect b c a || isCorrect c a b
    where isCorrect a b c = (a * a + b * b) == c * c
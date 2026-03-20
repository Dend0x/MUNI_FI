import Text.Parsec
import Text.Parsec.Char
import Text.Parsec.Combinator
import Text.Parsec.String

data Date = Date Int Int Int

parseDate :: Parsec Date
parseDate = do
    year <- read count 4 digit
    char '-'
    month <- read count 2 digit
    char '-'
    day <- read count 2 digit
    pure (Date year month day)
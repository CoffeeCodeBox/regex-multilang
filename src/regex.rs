// CoffeeCodeBox - Contributed By Amir Ali Vafaeian
use regex::Regex;

struct RegexEngine {
    text: String,
    regex: Regex,
}

impl RegexEngine {
    // the first arg is the text you wanna check. the second will be your regular expression
    fn new(txt: &str, rgx: &str) -> Self {
        let regex = Regex::new(rgx).unwrap();
        Self {
            text: txt.to_string(),
            regex,
        }
    }

    // returning if the text matches your pattern will be done using the is_match() METHOD in Rust
    fn test(&self) {
        println!(
            "the result of {:?} with the text of \"{}\" is {}",
            self.regex.as_str(),
            self.text,
            self.regex.is_match(&self.text)
        );
    }

    // returning the values matching your pattern will be done using the find_iter() METHOD in Rust
    fn show_matches(&self) {
        let matches: Vec<&str> = self.regex.find_iter(&self.text).map(|m| m.as_str()).collect();
        println!(
            "the regex {:?} for the text \"{}\" has these occurrences: {:?}",
            self.regex.as_str(),
            self.text,
            matches
        );
    }

    // replacing will be done using the replace_all() METHOD in Rust
    // suppose text has to be changed → the substrings matching regex will be replaced by txt
    fn replace(&mut self, replacement: &str) {
        self.text = self.regex.replace_all(&self.text, replacement).into_owned();
    }

    fn show_text(&self) {
        println!("REPLACED TEXT: {}", self.text);
    }
}

fn main() {
    // single word lookup
    let mut r = RegexEngine::new("hello man", "hello");
    r.test(); // true -> one word matches the pattern

    // various options (like the OR bitwise operator)
    let mut r = RegexEngine::new("I've got two dogs.", "cat|dog|bird|fish");
    r.test(); // true -> the "dog" will be found in the text

    ///////// NOTE: REGEX IS CASE SENSITIVE /////////

    // example
    let mut r = RegexEngine::new("I'VE GOT TWO DOGS", "cat|dog|bird|fish");
    r.test(); // false -> being case-sensitive, none of the words matches the pattern

    // telling it to be case insensitive, using "i" flag
    let mut r = RegexEngine::new("I'VE GOT TWO DOGS", "(?i)cat|dog|bird|fish");
    r.test(); // true -> being case-insensitive, the "DOG" word matches the pattern

    // extracting all matching occurrences in the text
    let mut r = RegexEngine::new("Twinkle, twinkle, little star...", "(?i)twinkle");
    r.show_matches(); // ["Twinkle", "twinkle"] -> returns all occurrences

    // finding words with wildcard characters -> e.g. /.un/ => run, pun, sun, gun etc.
    let mut r = RegexEngine::new("it should be fun to learn regular expressions during the sunset", ".un");
    r.show_matches(); // ["fun", "sun"] -> returns all occurrences

    // determining specific characters for the search, using []
    let mut r = RegexEngine::new("oh, boy! i see big bugs!", ".[auoie].");
    r.show_matches(); // ["boy", " i ", "see", "big", "bug"] -> returns all occurrences (vowels in this example)

    // determining a range of characters for the search, using DASH
    let mut r = RegexEngine::new("oh, boy! i see big bugs!", "[a-z]");
    r.show_matches(); // -> returns all of the letters in the text

    // including a combination of letters and numbers (b to f + 1 to 6)
    let mut r = RegexEngine::new("I've been there 4 the 2nd time", "[b-f1-6]");
    r.show_matches(); // [e,b,e,e,e,e,4,e,2,d,e] -> returns all occurrences

    // EXCLUDING A SET OF CHARACTERS FROM THE MATCH PICKUP

    // typically, you may wanna use ^ char to exclude a specified charset
    let mut r = RegexEngine::new("I was born in 2005", "[^0-9]");
    r.show_matches(); // -> returns all of the non-numeric characters in the text

    // SEARCHING FOR A *** ONCE-OR-MORE-TIMES-REPEATED *** CHARACTER

    // gotta use + sign right after the desired character
    let mut r = RegexEngine::new("Mississippi", "(?i)s+");
    r.show_matches(); // ["ss", "ss"]
    // adding an extra s to the end of the word
    let mut r = RegexEngine::new("Mississippis", "(?i)s+");
    r.show_matches(); // ["ss", "ss", "s"]

    // SEARCHING FOR A *** ZERO-OR-MORE-TIMES-REPEATED *** CHARACTER (OPTIONAL ACTUALLY)

    // gotta use * sign right after the desired character
    let mut r = RegexEngine::new("Google", "Go*");
    r.show_matches(); // ["Goo"]
    // adding i flag to the regex
    let mut r = RegexEngine::new("Google", "(?i)Go*");
    r.show_matches(); // ["Goo", "g"] -> being insensitive to the case, it includes every "g"

    // THERE ARE TWO TYPES OF EXTRACTING MATCHING EXPRESSIONS IN REGEX
    // 1.GREEDY 2.LAZY
    // GREEDY MATCH PICKS UP THE LONGEST MATCH IN THE TEXT
    // LAZY MATCH, ON THE OTHER HAND, PICKS UP THE SHORTEST MATCH IN THE TEXT
    // IMPORTANT: regex uses greedy match by default
    // greedy match example
    let mut r = RegexEngine::new("<p>hello</p>", "<.*>");
    r.show_matches(); // ["<p>hello</p>"]
    // using a question mark just before the last character to switch to LAZY MATCH
    let mut r = RegexEngine::new("<p>hello</p>", "<.*?>");
    r.show_matches(); // ["<p>"]
    // picking all of the matching parts
    let mut r = RegexEngine::new("<p>hello</p>", "<.*?>");
    r.show_matches(); // ["<p>", "</p>"]

    // checking if the text starts with the desired expression
    let mut r = RegexEngine::new("Alexa's been weak", "(?i)^alexa");
    r.test(); // true -> starts with "alexa" (case-insensitive)

    // checking if the text ends with the desired expression
    let mut r = RegexEngine::new("Alexa's been weak", "(?i)weak$");
    r.test(); // true -> ends with "weak"

    // picking lowercase and uppercase chars, numbers and underscores of a text
    // using SHORTHAND CHARACTERSET CLASS (\w)
    let mut r = RegexEngine::new("Hello my world!", "\\w");
    r.show_matches();
    println!("{}", r.regex.find_iter(&r.text).count()); // 12

    // doing the opposite: picking anything except the characters mentioned in the previous example
    // using \W class
    let mut r = RegexEngine::new("Hello my world!", "\\W");
    r.show_matches();
    println!("{}", r.regex.find_iter(&r.text).count()); // 3

    // accessing the numbers in a text
    // using \d class
    let mut r = RegexEngine::new("your order will be 12.99$", "\\d");
    r.show_matches();

    // accessing all non-numeric characters
    // using \D class
    let mut r = RegexEngine::new("your order will be 12.99$", "\\D");
    r.show_matches();

    // EXERCISE: VALIDATE USERNAMES WITH 3 CONDITIONS:
    // 1. letters come first and then numbers(which are optional)
    // 2. letters could be uppercase or lowercase
    // 3. minimum length of the letters should be 2
    // The answer:
    let mut r = RegexEngine::new("CoffeeCodeBox23", "(?i)^[a-z]{2,}\\d*$");
    r.test();

    // accessing the whitespaces(spaces, newlines, tabs, etc.)
    // using \s class
    let mut r = RegexEngine::new("your order will be 12.99$", "\\s");
    r.show_matches();

    // HOW TO WORK WITH QUANTITY SPECIFIERS
    // YOU COULD SPECIFY HOW MANY TIMES A SINGLE CHARACTER OF A CHARACTERSET SHOULD MATCH A PATTERN
    // in these examples, we determine how many time should "l" be repeated
    // 1. using a definite value
    let mut r = RegexEngine::new("hellllo!", "^hel{2}o!");
    r.test(); // false -> 2 != 4
    // 2. using a range -> the first value is the min and second one is the max (optional)
    let mut r = RegexEngine::new("hellllo!", "^hel{2,4}o!");
    r.test(); // true -> 2 < 4 <= 4

    // EXERCISE: validate emails using regex
    // THE ANSWER:
    let mut r = RegexEngine::new("myemail@host.com", "(?i)^[a-z]{1,}[a-z0-9_]{2,}@[a-z]{2,15}[.]{1}[a-z]{2,8}$");
    r.test(); // true -> it's valid

    // checking the possible existence of a character with a ?
    let mut r = RegexEngine::new("favourite", "favou?rite");
    r.test(); // true, even if you remove the letter "u"

    // REPLACEMENT
    // example
    let mut r = RegexEngine::new("the silver sky", "silver");
    r.replace("blue");
    r.show_text();

}


// Congrats! You can now effectively use regex — keep learning and good luck!
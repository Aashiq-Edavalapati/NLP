# 📚 Regular Expressions (Regex)

Regular Expressions (often shortened to "Regex" or "RegExp") are powerful patterns used for searching, matching, and manipulating text. They are a sequence of characters that define a search pattern, primarily used for "find and replace" operations, input validation, and parsing of textual data. In Natural Language Processing (NLP), regex is an invaluable tool for tasks like tokenization, pattern extraction, data cleaning, and feature engineering.

-----

## 🔍 What is Regular Expressions?

Regex provides a concise and flexible way to identify patterns in strings. Instead of searching for exact literal strings, you can define patterns that match variations, specific character types, repetitions, or positions within a text.

### Basic Components and Syntax:

Regex patterns are built using a combination of literal characters and special characters (metacharacters) that have predefined meanings.

#### Literal Characters:

  * Any character that is not a metacharacter matches itself.
      * `cat` matches "cat" in "The cat sat on the mat."

#### Metacharacters:

These characters have special meanings and allow for more complex pattern matching.

  * **Anchors:**

      * `^`: Matches the beginning of a string.
          * `^The` matches "The" at the start of "The quick brown fox."
      * `$`: Matches the end of a string.
          * `fox.$` matches "fox." at the end of "The quick brown fox."
      * `\b`: Word boundary. Matches the position between a word character and a non-word character (or start/end of string).
          * `\bcat\b` matches "cat" in "The cat." but not "catamaran".

  * **Quantifiers:** Specify how many times a character or group can occur.

      * `*`: Zero or more occurrences.
          * `ab*c` matches "ac", "abc", "abbc", etc.
      * `+`: One or more occurrences.
          * `ab+c` matches "abc", "abbc", but not "ac".
      * `?`: Zero or one occurrence (optional).
          * `colou?r` matches "color" and "colour".
      * `{n}`: Exactly `n` occurrences.
          * `a{3}` matches "aaa".
      * `{n,}`: `n` or more occurrences.
          * `a{2,}` matches "aa", "aaa", etc.
      * `{n,m}`: Between `n` and `m` occurrences (inclusive).
          * `a{1,3}` matches "a", "aa", "aaa".

  * **Character Classes:** Match any one of a set of characters.

      * `.`: Any character except newline.
          * `a.b` matches "axb", "a\#b", "a b", etc.
      * `[abc]`: Matches 'a', 'b', or 'c'. (Character set)
          * `[aeiou]` matches any lowercase vowel.
      * `[^abc]`: Matches any character *not* 'a', 'b', or 'c'. (Negated character set)
          * `[^0-9]` matches any non-digit character.
      * `[a-z]`: Matches any lowercase letter from 'a' to 'z'. (Range)
      * `[A-Z]`: Matches any uppercase letter from 'A' to 'Z'.
      * `[0-9]`: Matches any digit from '0' to '9'.
          * Shorthand: `\d` (digit)
          * `\D` (non-digit)
      * `\w`: Matches any word character (alphanumeric + underscore). `[a-zA-Z0-9_]`
          * `\W` (non-word character)
      * `\s`: Matches any whitespace character (space, tab, newline, etc.).
          * `\S` (non-whitespace character)

  * **Alternation:**

      * `|`: OR operator. Matches either the expression before or after the `|`.
          * `cat|dog` matches "cat" or "dog".

  * **Grouping and Capturing:**

      * `( )`: Groups sub-expressions. Can be used with quantifiers or for capturing matched text.
          * `(ab)+` matches "ab", "abab", "ababab", etc.

  * **Escaping Special Characters:**

      * `\`: Used to escape metacharacters if you want to match them literally.
          * `\$` matches a literal '$'. `\.` matches a literal '.'.

### Example: Email Validation Pattern

A simple (but not exhaustive) regex for validating an email address:
`[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`

  * `[a-zA-Z0-9._%+-]+`: Matches one or more alphanumeric characters, dots, underscores, percents, plus signs, or hyphens (username part).
  * `@`: Matches the literal '@' symbol.
  * `[a-zA-Z0-9.-]+`: Matches one or more alphanumeric characters, dots, or hyphens (domain name).
  * `\.`: Matches a literal dot.
  * `[a-zA-Z]{2,}`: Matches 2 or more letters (top-level domain like "com", "org", "net").

-----

## 💡 How Regex is Used in NLP

Regex is extremely versatile in NLP for various text manipulation and extraction tasks:

  * **Tokenization:** Splitting text into words, sentences, or other meaningful units while handling punctuation.
      * Example: Splitting by spaces and removing trailing punctuation: `re.findall(r'\b\w+\b', text)`
  * **Data Cleaning:**
      * Removing HTML tags: `re.sub(r'<.*?>', '', html_text)`
      * Removing special characters: `re.sub(r'[^a-zA-Z0-9\s]', '', text)`
      * Standardizing whitespace: `re.sub(r'\s+', ' ', text)`
  * **Pattern Extraction:**
      * Extracting dates, phone numbers, email addresses.
      * Finding hashtags or mentions in social media text.
      * Identifying specific phrases or sequences of words.
  * **Lexicon-based Analysis:** Creating rules to identify terms for sentiment analysis or named entity recognition.
  * **Preprocessing for Machine Learning:** Preparing raw text into a cleaner format suitable for model input.

-----

## 🛠 Implementation Approaches

Most programming languages (including Python, Java, JavaScript, Perl, Ruby, etc.) have built-in support for regular expressions.

In **Python**, the `re` module is used for regex operations:

  * `re.search(pattern, string)`: Scans through string looking for the first location where the pattern produces a match.
  * `re.match(pattern, string)`: Checks for a match only at the beginning of the string.
  * `re.findall(pattern, string)`: Returns all non-overlapping matches of pattern in string, as a list of strings.
  * `re.sub(pattern, repl, string)`: Replaces occurrences of pattern in string with `repl`.
  * `re.compile(pattern)`: Compiles a regular expression pattern into a regular expression object, which can be used for more efficient repeated searching.

**[Link to Regex Implementation: `implementations/regex_implementation.py`](https://www.google.com/search?q=./implementations/regex_implementation.py)** (You'll need to create this file with your implementation)

-----

## 🌟 Why It’s Useful

  * **Flexibility:** Can define highly specific and complex search patterns.
  * **Efficiency:** Highly optimized for pattern matching within text.
  * **Ubiquity:** Supported across almost all programming languages and text editors.
  * **Text Preprocessing:** Essential for cleaning and preparing raw text data for further NLP analysis.
  * **Information Extraction:** Enables structured extraction of data from unstructured text.

-----

## 🔗 Further Reading

  * [Python `re` module documentation](https://www.google.com/search?q=%5Bhttps://docs.python.org/3/library/re.html%5D\(https://docs.python.org/3/library/re.html\))
  * [RegexOne - Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)
  * [MDN Web Docs - Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions) (General concepts are universal)
  * [Regular-Expressions.info - The \#1 Reference](https://www.regular-expressions.info/)

-----

📂 This markdown provides a comprehensive overview of Regular Expressions, their syntax, how they function, and their crucial role in various NLP tasks, along with practical implementation notes.

**You can find the implementation [here](../implementations/Regular%20Expressions/regex.py)**
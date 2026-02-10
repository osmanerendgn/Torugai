# AI Code Review Assignment (Python)

## Candidate
- Name: Osman Eren Doğan
- Approximate time spent: 3 hours

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
Logic Error (Denominator Bias): The function filters the numerator (sum of amounts) but uses the total count of all orders (len(orders)) as the denominator. This results in an incorrectly deflated average because cancelled orders are excluded from the total sum but included in the count.
ZeroDivisionError: The function crashes if the input list is empty or if it contains only cancelled orders, as it attempts to divide by zero.

### Edge cases & risks
Empty Input: Not handled, leading to a fatal crash.
Direct dictionary access (order["status"]) may raise KeyError if the field is missing.
If all orders are cancelled, the function still attempts division.

### Code quality / design issues
Inefficiency: The calculation is mathematically inconsistent.
Lack of Robustness: No input validation or safe dictionary access.
Error handling is missing for malformed or incomplete order entries.

## 2) Proposed Fixes / Improvements
### Summary of changes
Implemented a filtered count to ensure the denominator matches the numerator.
Added a guard clause to return 0.0 for empty or fully-cancelled lists.
Utilized .get() for safer dictionary access to prevent KeyError.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

Empty input list
All orders cancelled
Mixed cancelled and non-cancelled orders
Orders with missing or malformed fields
Non-numeric order amounts


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
The denominator is incorrect and includes cancelled orders.
Edge cases such as empty input or all-cancelled orders are ignored.

### Rewritten explanation
This function calculates the average order value by considering only non-cancelled orders for both the total amount and the count. Cancelled orders are fully excluded from the calculation, and the function safely returns 0.0 when no valid orders are present.

## 4) Final Judgment
- Decision: Reject
- Justification: The original code contains a critical logical error that produces incorrect averages and lacks basic error handling.
- Confidence & unknowns: Normal confidence. The logic error is a classic "denominator bias" bug.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
Insufficient Validation: Only checks for the presence of "@". This allows invalid entries like "@@", "user@", or "@domain.com" to pass.
It raises TypeError when encountering non-string inputs such as None or integers.

### Edge cases & risks
Emails with leading/trailing whitespace are not handled.
Empty or null values are not safely ignored.
Performance: Standard Python for loops are inefficient for large-scale email validation datasets.

### Code quality / design issues
The AI claims to "safely ignore invalid entries" but actually crashes on mixed data types.
Uses a Python loop instead of vectorized operations, which is inefficient for larger datasets.

## 2) Proposed Fixes / Improvements
### Summary of changes
Converted the input list into a Pandas Series to leverage vectorized string operations for performance.
Applied a regular expression via Series.str.match to enforce a basic email structure.
Normalized inputs using dropna(), astype(str), and str.strip().
Added explicit input validation using isinstance(emails, list).
Avoided external NLP or parsing libraries (BeautifulSoup, bs4, nltk, spaCy, neattext/nfx) in alignment with assignment requirements.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

Empty input list
Mixed-type inputs (None, integers, strings)
Clearly invalid email formats
Valid emails with surrounding whitespace
Large input size for performance validation

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
The function does not safely ignore invalid entries.
The validation logic does not align with any reasonable definition of a valid email.

### Rewritten explanation
This optimized version utilizes Pandas Series to leverage vectorized string operations, significantly increasing processing speed. It ensures type safety by cleaning the data (dropping NaNs and stripping spaces) and applies a robust Regular Expression to validate the standard email format.
External NLP/parsing libraries (e.g., BeautifulSoup, nfx/neattext) were intentionally avoided. While they are powerful for extraction, introducing them for a narrow validation task adds unnecessary dependencies. This solution relies on the standard re module and pandas for optimal engineering balance.

## 4) Final Judgment
- Decision: Reject
- Justification: The AI-generated code is structurally flawed, unsafe for mixed inputs, and fails to meet even minimal expectations for email validation.
- Confidence & unknowns: High confidence. Vectorization is the industry standard for this type of data processing.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
The function divides by len(values) even though None values are excluded from the aggregation.
Unsafe Conversion: float(v) raises a ValueError if a string that cannot be converted to a number is encountered.
ZeroDivisionError: Crashes on empty lists or lists with no valid numeric data.

### Edge cases & risks
Raises ZeroDivisionError for empty input or when all values are invalid. ["10.5", "invalid", None] causes a crash.
Empty Data: Not handled.

### Code quality / design issues
The code provides a "silent error" (incorrect result) which is more dangerous than a crash in data engineering.
Error handling for mixed-type inputs is missing.
The denominator logic does not reflect the filtered data.


## 2) Proposed Fixes / Improvements
### Summary of changes
Converted input into a Pandas Series for vectorized numeric processing.
Used pd.to_numeric(..., errors="coerce") to safely coerce invalid values to NaN.
Removed invalid values using dropna().
Applied Series.mean(), which correctly handles the denominator by only counting valid numeric entries.
Validated input to ensure it is a non-empty list.
Returned 0.0 when no valid measurements exist.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
Empty input
All values None
Mixed numeric and non-numeric values
Numeric strings
Large datasets for stability

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
Mathematically False: It does not ensure an "accurate average" due to the denominator bug.
Safety Halucination: It does not "safely handle mixed types"; it crashes on non-numeric strings.

### Rewritten explanation
This function computes the true arithmetic mean of valid numeric measurements. It uses Pandas to coerce non-numeric values to NaN safely and removes them. The final average is calculated using only the remaining numeric values, ensuring statistical accuracy and preventing division-by-zero errors.

## 4) Final Judgment
- Decision: Reject
- Justification: The original implementation produces mathematically incorrect averages, which is more dangerous than a runtime failure in data-driven systems.
- Confidence & unknowns: High confidence. The error directly violates the function’s stated purpose.

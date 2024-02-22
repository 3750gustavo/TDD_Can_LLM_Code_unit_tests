### First Test: Refactoring with the DRY Principle

**Instruction Prompt:**

Review the provided Python code, which includes multiple functions related to handling a shopping cart system. Each function has some level of repetitive logic or code. Your task is to refactor the code by applying the 'Do Not Repeat Yourself' (DRY) principle. Aim to reduce redundancy and simplify the code structure without compromising its functionality. Ensure that the refactored code maintains all original capabilities, including calculating total prices, applying taxes, and discounts where applicable:

```python
def calculate_total_price(items):
    total = 0
    for item in items:
        total += item['price']
    return total

def calculate_total_with_tax(items, tax):
    total = calculate_total_price(items)
    tax_amount = total * tax
    return total + tax_amount

def calculate_total_with_discount(items, discount):
    total = calculate_total_price(items)
    discount_amount = total * discount
    return total - discount_amount
```

### Second Test: Code Optimization for Performance and Readability

**Instruction Prompt:**

Examine the given Python function designed to categorize a list of users by age groups. The current implementation uses a series of conditional statements to determine each user's age group and then categorizes them accordingly. Your objective is to optimize this code to improve both performance and readability. Focus on making the code more concise and efficient, ensuring that it's easily understandable and maintainable. The optimized solution should continue to accurately categorize users into the predefined age groups without any loss of functionality:

```python
def categorize_users_by_age(users):
    categorized = {'child': [], 'teen': [], 'adult': [], 'senior': []}
    for user in users:
        if user['age'] < 13:
            categorized['child'].append(user)
        elif user['age'] >= 13 and user['age'] < 20:
            categorized['teen'].append(user)
        elif user['age'] >= 20 and user['age'] < 65:
            categorized['adult'].append(user)
        else:
            categorized['senior'].append(user)
    return categorized
```
# Unit Tests Python Code Optimization Stage

The second stage of LLM tests focuses on assessing the Large Language Models' ability to refine and optimize existing code. This phase includes two tests tailored to evaluate the application of coding principles and the enhancement of code performance or readability.

### First Test: Refactoring with the DRY Principle

The aim is to assess the LLM's skill in applying the 'Do Not Repeat Yourself' (DRY) principle to refactor given code effectively. Consider the scenario where repetitive logic exists across multiple functions related to handling a shopping cart system:

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

The LLM should consolidate the repetitive logic into a more cohesive, DRY-compliant structure, reducing redundancy while maintaining functionality:

```python
def calculate_total_price(items, tax=0, discount=0):
    total = sum(item['price'] for item in items)
    if tax > 0:
        total += total * tax
    if discount > 0:
        total -= total * discount
    return total
```

This refactored version introduces a single function handling all price calculations, integrating tax and discount computations as optional parameters. It exemplifies the DRY principle by eliminating repeated code and enhancing maintainability.

### Second Test: Code Optimization for Performance and Readability

This test evaluates the LLM's capability to optimize code, focusing on improving performance and readability. Consider a function designed to categorize users based on age groups:

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

The LLM should enhance this function for better performance and readability. A possible improvement involves streamlining the age categorization logic and utilizing more Pythonic constructs:

```python
def categorize_users_by_age(users):
    categories = {'child': (0, 12), 'teen': (13, 19), 'adult': (20, 64), 'senior': (65, float('inf'))}
    categorized = {category: [] for category in categories}
    for user in users:
        for category, (min_age, max_age) in categories.items():
            if min_age <= user['age'] <= max_age:
                categorized[category].append(user)
                break
    return categorized
```

This optimized version employs a dictionary to map age ranges to categories, simplifying the categorization logic and improving code readability. It demonstrates effective use of Python's features to achieve a concise and efficient solution.

---

These enhanced tests are crafted to push the boundaries of LLM's coding proficiency, focusing on principles, efficiency, and the practical application of Pythonic idioms.
from functools import wraps

# 1. გლობალური ცვლადები
SYSTEM_ACTIVE = True
GLOBAL_AUDIT_LOG = []

# 2. დეკორატორი
def audit_system(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if SYSTEM_ACTIVE:
            GLOBAL_AUDIT_LOG.append(f"Function called: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# 3. გარე ფუნქცია (Closure & Enclosing)
def create_account_generator(initial_balance):
    balance = initial_balance
    transaction_id = 0

    # 4. შიდა გენერატორი
    @audit_system
    def transaction(amount):

        nonlocal balance, transaction_id

        balance += amount
        transaction_id += 1

        yield (
            transaction_id,
            amount,
            balance
        )

    return transaction



account = create_account_generator(1000)

print(next(account(200)))
print(next(account(-100)))
print(next(account(500)))


print(GLOBAL_AUDIT_LOG)
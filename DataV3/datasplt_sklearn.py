from sklearn.model_selection import train_test_split

# Assuming you have your data stored in variables X and y
# Splitting the data into training and testing sets with a 80:20 ratio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Splitting the training set into training and validation sets with a 75:25 ratio
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=42)

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Sample data (replace with your own dataset)
emails = ["Buy our amazing products now!",
          "Congratulations! You've won $1000.",
          "Hello, how are you doing?",
          "Discounts on luxury watches!",
          "Meeting at 3 pm today."]

labels = [1, 1, 0, 1, 0]  # 1 for spam, 0 for not spam

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(emails, labels, test_size=0.2, random_state=42)

# Create a TF-IDF Vectorizer to convert text to numerical features
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Create an SVM classifier
svm_classifier = SVC(kernel='linear', C=1.0)

# Train the SVM classifier
svm_classifier.fit(X_train_tfidf, y_train)

# Make predictions on the test data
y_pred = svm_classifier.predict(X_test_tfidf)

# Calculate accuracy and display the results
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

confusion = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(confusion)

classification_rep = classification_report(y_test, y_pred)
print("Classification Report:")
print(classification_rep)

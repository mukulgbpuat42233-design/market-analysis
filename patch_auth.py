import sys

with open('index.html', 'r') as f:
    content = f.read()

old_auth = """onAuthStateChanged(auth, async (user) => {"""
new_auth = """onAuthStateChanged(auth, async (user) => {
      // Create handleFirestoreError for future robust error handling as per rules
      window.handleFirestoreError = function(error, operationType, path) {
        const errInfo = {
          error: error instanceof Error ? error.message : String(error),
          authInfo: {
            userId: auth.currentUser?.uid,
            email: auth.currentUser?.email,
            emailVerified: auth.currentUser?.emailVerified
          },
          operationType,
          path
        };
        console.error('Firestore Error: ', JSON.stringify(errInfo));
      };
"""

content = content.replace(old_auth, new_auth)
with open('index.html', 'w') as f:
    f.write(content)
